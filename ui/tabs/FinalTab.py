
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


class FinalTab(Tab.Tab):
    def __init__(self, classes):
        super().__init__("Finalize", None)

        self.__classes = classes

        self.addItemToLayout(QtWidgets.QLabel("path"), 2, 0)

        path_input = QtWidgets.QLineEdit()
        path_input.textChanged.connect(self.__setPath)
        self.addItemToLayout(path_input, 2, 1)

        button = QtWidgets.QPushButton("Finalize")
        button.clicked.connect(self.__submit)
        self.addItemToLayout(button, 0, 1)
    

    def __setPath(self, text):
        for cla in self.__classes:
            cla.setPath(text)

    def __submit(self):
        for cla in self.__classes:
            if cla.getOption():
                cla.print()
        