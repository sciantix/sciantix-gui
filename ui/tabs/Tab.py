
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


class Tab(QtWidgets.QWidget):
    def __init__(self, name: str, classe):
        super().__init__()

        self.__name   = name
        # To have access to the business logic since we cannot import from outside the ui module
        self._class  = classe
        self.__layout = QtWidgets.QGridLayout()

        self.setLayout(self.__layout)
    

    def getName(self) -> str:
        return self.__name 
    
    def addItemToLayout(self, new_item, row: int, column: int):
        self.__layout.addWidget(new_item, row, column)
        self.setLayout(self.__layout)
    
    def addToTabList(self, tab_list: list):
        tab_list.addTab(self, self.__name)
