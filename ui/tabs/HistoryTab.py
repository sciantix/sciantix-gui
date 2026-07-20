
"""
----------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __      ___     .__   __..___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |    /   \    |  \ |  ||           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |   /  ^  \   |   \|  |`---|  |----`   \  \   ^   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |  /  /_\  \  |  . `  |    |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  )  |
.----)   |   |  `----.|  | /  _____  \ |  |\   |    |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__|/__/     \__\|__| \__|    |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

----------------------------------------------------------------------------------------------------------------------------------

    Originally developed by G. Léandre

    Version : 1.4.5
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtWidgets as QtWidgets

from . import ScrollableIETab


class HistoryTab(ScrollableIETab.ScrollableIETab):
    __slots__ = [
        # From the Tab super-class
        "__name",
        "__class",
        "__layout",
        "_option",
        # From the ScrollableTab super-class
        "__group_box",
        "__scroll",
        # From the ImportExportTab super-class
    ]

    def __init__(self, history_class):
        super().__init__("Input History", history_class)

        button = QtWidgets.QPushButton("Add Line")
        button.clicked.connect(self.__addLine)
        self.addItemToLayout(button, 1, 0)

        button = QtWidgets.QPushButton("Toggle Steam Pressure")
        button.clicked.connect(self.__toggleSteamPressure)
        self.addItemToLayout(button, 1, 5)

        for i, name in enumerate(self._getClass().getLineNames()):
            if self._getClass().getUnits():
                self.addItemToLayout(QtWidgets.QLabel(f"{self._pretifyText(name)} in {self._getClass().getUnits()[i]}"), 2, i)
            else:
                self.addItemToLayout(QtWidgets.QLabel(self._pretifyText(name)), 2, i)

        for i in range(self._getClass().getNbrLines()):
            self.__makeLine(i)

    
    def __makeLine(self, force_index: int = -1):
        index = self._getClass().getNbrLines()

        if -1 > force_index or force_index > index :
            raise IndexError("Index out of range, the index has to be between -1 and the number of lines from the associated class")
        elif force_index > -1:
            index = force_index+1
            
        names  = self._getClass().getLineNames()
        values = self._getClass().getLineByNbr(index-1)


        for i in range(len(names)):
            current_input = QtWidgets.QLineEdit(str(values[i]))
            current_input.textChanged.connect(
                (lambda name, index:
                    lambda text: self._getClass().trySetValueByName(f"{index-1}{name}", text)
                )(names[i], index)
            )
            self.addItemToLayout(current_input, index+2, i)

        if index != 1:
            button = QtWidgets.QPushButton("Remove")
            button.clicked.connect(lambda: self.__removeLineByIndex(index+2))
            self.addItemToLayout(button, index+2, 5)
    
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
                self.removeItemFromLayout(index, column)
        
        self._getClass().deleteLineByNbr(index-3)

        # Adjusting the layout
        for row in range(index, nbr_of_lines+2):
            for column in range(6):
                if (column != 4) or self._getClass().hasSteamPressure():
                    self.moveItemInLayout(row+1, column, row, column)

            # To have the button remove function have the correct row/index number
            self.removeItemFromLayout(row, 5)
            button = QtWidgets.QPushButton("Remove")
            button.clicked.connect((lambda index: lambda: self.__removeLineByIndex(index))(row))
            self.addItemToLayout(button, row, 5)

    def __toggleSteamPressure(self):
        self._getClass().toggleSteamPressure()

        if self._getClass().hasSteamPressure():
            self.__addSteamPressure()
        else:
            self.__removeSteamPressure()

    def __addSteamPressure(self):
        self.addItemToLayout(QtWidgets.QLabel("Steam Pressure"), 2, 4)

        for i in range(self._getClass().getNbrLines()):
            current_input = QtWidgets.QLineEdit(str(self._getClass().getValueByName(f"{i}steam_pressure")))
            current_input.textChanged.connect(
                (lambda index:
                    lambda text: self._getClass().trySetValueByName(f"{index}steam_pressure", text)
                )(i)
            )
            self.addItemToLayout(current_input, i+3, 4)

    def __removeSteamPressure(self):
        self.removeItemFromLayout(2, 4)

        for i in range(self._getClass().getNbrLines()):
            self.removeItemFromLayout(i+3, 4)
