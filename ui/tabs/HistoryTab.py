
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

    Version : 1.0.0
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtWidgets as QtWidgets

from . import Tab


class HistoryTab(Tab.Tab):
    def __init__(self, history_class):
        super().__init__("Input History", history_class)

        button = QtWidgets.QPushButton("Add Line")
        button.clicked.connect(self.__addLine)
        self.addItemToLayout(button, 0, 0)

        button = QtWidgets.QPushButton("Add Steam Pressure")
        button.clicked.connect(self.__toggleSteamPressure)
        self.addItemToLayout(button, 0, 5)

        for i, name in enumerate(self._class.getLineNames()):
            self.addItemToLayout(QtWidgets.QLabel(name), 1, i)

        self.__makeLine()

    
    def __makeLine(self):
        index = self._class.getNbrLines()

        names  = self._class.getLineNames()
        values = self._class.getLineByNbr(index-1)

        for i in range(len(names)):
            current_input = QtWidgets.QLineEdit(str(values[i]))
            current_input.textChanged.connect(
                (lambda name, index:
                    lambda text: self._class.setValueByName(f"{index-1}{name}", int(text) if (len(text) != 0) else 0)
                )(names[i], index)
            )
            self.addItemToLayout(current_input, index+1, i)

        if index != 1:
            button = QtWidgets.QPushButton("Remove")
            button.clicked.connect(lambda: self.__removeLineByIndex(index))
            self.addItemToLayout(button, index+1, 5)
    
    def __addLine(self):
        if (self._class.hasSteamPressure()):
            self._class.addLine(0, 0, 0, 0, 0)
        else:
            self._class.addLine(0, 0, 0, 0)

        self.__makeLine()
    
    def __removeLineByIndex(self, index: int):
        nbr_of_lines = self._class.getNbrLines()

        for column in range(6):
            if (column != 4) or self._class.hasSteamPressure():
                self.removeItemFromLayout(index+1, column)
        
        self._class.deleteLineByNbr(index-1)

        # adjusting the layout
        for row in range(index+1, nbr_of_lines+1):
            for column in range(6):
                if (column != 4) or self._class.hasSteamPressure():
                    self.moveItemInLayout(row+1, column, row, column)

    def __toggleSteamPressure(self):
        if self._class.hasSteamPressure():
            self.__removeSteamPressure()
        else:
            self.__addSteamPressure()

    def __addSteamPressure(self):
        self._class.toggleSteamPressure()
        
        self.addItemToLayout(QtWidgets.QLabel("steam_pressure"), 1, 4)

        for i in range(self._class.getNbrLines()):
            current_input = QtWidgets.QLineEdit(str(self._class.getValueByName(f"{i}steam_pressure")))
            current_input.textChanged.connect(
                (lambda index:
                    lambda text: self._class.setValueByName(f"{index}steam_pressure", int(text) if (len(text) != 0) else 0)
                )(i)
            )
            self.addItemToLayout(current_input, i+2, 4)

    def __removeSteamPressure(self):
        self._class.toggleSteamPressure()
        
        self.removeItemFromLayout(1, 4)

        for i in range(self._class.getNbrLines()):
            self.removeItemFromLayout(i+2, 4)
