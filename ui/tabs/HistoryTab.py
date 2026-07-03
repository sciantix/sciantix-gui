
"""
-------------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __       ___      .__   __. .___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |     /   \     |  \ |  | |           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |    /  ^  \    |   \|  | `---|  |----`   \  \   ^   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |   /  /_\  \   |  . `  |     |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  )  |
.----)   |   |  `----.|  |  /  _____  \  |  |\   |     |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__| /__/     \__\ |__| \__|     |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

-------------------------------------------------------------------------------------------------------------------------------------

    Originally developed by G. Léandre

    Version : 1.4.0
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtWidgets as QtWidgets

from . import ScrollableTab


class HistoryTab(ScrollableTab.ScrollableTab):
    def __init__(self, history_class):
        super().__init__("Input History", history_class)

        button = QtWidgets.QPushButton("Add Line")
        button.clicked.connect(self.__addLine)
        self.addItemToLayout(button, 0, 0)

        button = QtWidgets.QPushButton("Toggle Steam Pressure")
        button.clicked.connect(self.__toggleSteamPressure)
        self.addItemToLayout(button, 0, 5)

        for i, name in enumerate(self._getClass().getLineNames()):
            self.addItemToLayout(QtWidgets.QLabel(name), 1, i)

        self.__makeLine()

    
    def __makeLine(self):
        index = self._getClass().getNbrLines()

        names  = self._getClass().getLineNames()
        values = self._getClass().getLineByNbr(index-1)

        for i in range(len(names)):
            current_input = QtWidgets.QLineEdit(str(values[i]))
            current_input.textChanged.connect(
                (lambda name, index:
                    lambda text: self._getClass().setValueByName(f"{index-1}{name}", int(text) if (len(text) != 0) else 0)
                )(names[i], index)
            )
            self.addItemToLayout(current_input, index+1, i)

        if index != 1:
            button = QtWidgets.QPushButton("Remove")
            button.clicked.connect(lambda: self.__removeLineByIndex(index))
            self.addItemToLayout(button, index+1, 5)
    
    def __addLine(self):
        if (self._getClass().hasSteamPressure()):
            self._getClass().addLine(0, 0, 0, 0, 0)
        else:
            self._getClass().addLine(0, 0, 0, 0)

        self.__makeLine()
    
    def __removeLineByIndex(self, index: int):
        nbr_of_lines = self._getClass().getNbrLines()

        for column in range(6):
            if (column != 4) or self._getClass().hasSteamPressure():
                self.removeItemFromLayout(index+1, column)
        
        self._getClass().deleteLineByNbr(index-1)

        # adjusting the layout
        for row in range(index+1, nbr_of_lines+1):
            for column in range(6):
                if (column != 4) or self._getClass().hasSteamPressure():
                    self.moveItemInLayout(row+1, column, row, column)

    def __toggleSteamPressure(self):
        if self._getClass().hasSteamPressure():
            self.__removeSteamPressure()
        else:
            self.__addSteamPressure()

    def __addSteamPressure(self):
        self._getClass().toggleSteamPressure()
        
        self.addItemToLayout(QtWidgets.QLabel("steam_pressure"), 1, 4)

        for i in range(self._getClass().getNbrLines()):
            current_input = QtWidgets.QLineEdit(str(self._getClass().getValueByName(f"{i}steam_pressure")))
            current_input.textChanged.connect(
                (lambda index:
                    lambda text: self._getClass().setValueByName(f"{index}steam_pressure", int(text) if (len(text) != 0) else 0)
                )(i)
            )
            self.addItemToLayout(current_input, i+2, 4)

    def __removeSteamPressure(self):
        self._getClass().toggleSteamPressure()
        
        self.removeItemFromLayout(1, 4)

        for i in range(self._getClass().getNbrLines()):
            self.removeItemFromLayout(i+2, 4)
