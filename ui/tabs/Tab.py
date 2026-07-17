
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

    Version : 1.4.4
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtCore    as QtCore
import PyQt6.QtWidgets as QtWidgets


class Tab(QtWidgets.QWidget):
    def __init__(self, name: str, classe):
        super().__init__()

        self.__name   = name
        self._option  = True
        # To have access to the business logic since we cannot import from outside the ui module
        self.__class   = classe
        
        self.__layout = QtWidgets.QGridLayout()

        self.__layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.__layout.setVerticalSpacing(5)

        self.setLayout(self.__layout)


    def getName(self) -> str:
        return self.__name 

    def getOption(self) -> bool:
        return self._option
    
    def _getClass(self):
        return self.__class
    
    def _getLayout(self):
        return self.__layout

    def addItemToLayout(self, new_item, row: int, column: int):
        self.__layout.addWidget(new_item, row, column)
        # self.setLayout(self.__layout)
    
    def removeItemFromLayout(self, row: int, column: int):
        self.__layout.removeWidget(self.__layout.itemAtPosition(row, column).widget())
    
    def moveItemInLayout(self, row: int, column: int, new_row: int, new_column: int):
        temp = self.__layout.itemAtPosition(row, column).widget()
        self.__layout.removeWidget(temp)
        self.addItemToLayout(temp, new_row, new_column)

    def addToTabList(self, tab_list: list):
        tab_list.addTab(self, self.__name)
        
    def setPath(self, path: str):
        self.__class.setPath(path)
        
    def print(self):
        self.__class.print()

    def _pretifyText(self, text: str) -> str:
        """
        Take a cammel case or snake case string like : GetOptionsNames or get_options_names
        and insert spaces in between the words to make easier to read like : Get Options Names
        """
        new_text = ""

        for letter in text:
            if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ_":
                new_text += " "
            if letter != '_':
                new_text += letter

        return new_text
