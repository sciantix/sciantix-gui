
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

    Version : 1.1.0
    Year :    2026
    Authors : G. Léandre
"""


import os
import PyQt6.QtWidgets as QtWidgets

from . import Tab
from .. import config


class FinalTab(Tab.Tab):
    def __init__(self, classes):
        super().__init__("Finalize", None)

        self.__classes = classes

        self.__setPath(config.DEFAULT_OUTPUT_PATH)

        self.addItemToLayout(QtWidgets.QLabel("Path"), 0, 0)

        path_input = QtWidgets.QLineEdit(config.DEFAULT_OUTPUT_PATH)
        path_input.textChanged.connect(self.__setPath)
        self.addItemToLayout(path_input, 0, 1)

        button = QtWidgets.QPushButton("Build Input Files")
        button.clicked.connect(self.__submit)
        self.addItemToLayout(button, 1, 1)

        button = QtWidgets.QPushButton("Build and Run the Simulation")
        button.clicked.connect(self.__runSciantix)
        self.addItemToLayout(button, 2, 1)
    

    def __setPath(self, text):
        for cla in self.__classes:
            cla.setPath(text)

    def __submit(self):
        for cla in self.__classes:
            if cla.getOption():
                cla.print()

    def __runSciantix(self):
        # To clean the input and output files
        os.system("rm sciantix/*.txt")

        self.__setPath("sciantix")
        self.__submit()
        os.system("sciantix/sciantix.x sciantix/")
        