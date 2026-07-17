
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

import os
import PyQt6.QtGui     as QtGui
import PyQt6.QtWidgets as QtWidgets

from . import Tab
from .. import config


class VisualisationTab(Tab.Tab):
    __slots__ = [
        # From the Tab super-class
        "__name",
        "__class",
        "__layout",
        "_option",

        # From the VisualisationTab class
        "__output",
        "__x_name",
        "__y_name",
        "__label",
    ]

    def __init__(self, output):
        super().__init__("Visualize", None)

        self.__output = output

        self.__x_name = self.__output._getClass().getLineNames()[0]
        self.__y_name = self.__output._getClass().getLineNames()[1]

        self.addItemToLayout(QtWidgets.QLabel("x value"), 0, 0)
        x_input = QtWidgets.QComboBox()
        x_input.addItems(self.__output._getClass().getLineNames())
        x_input.currentTextChanged.connect(self.__setXName)
        self.addItemToLayout(x_input, 0, 1)

        self.addItemToLayout(QtWidgets.QLabel("y value"), 1, 0)
        y_input = QtWidgets.QComboBox()
        y_input.addItems(self.__output._getClass().getLineNames())
        y_input.currentTextChanged.connect(self.__setYName)
        self.addItemToLayout(y_input, 1, 1)

        self.__label = QtWidgets.QLabel(self)
        self.__label.setPixmap(QtGui.QPixmap(f"{self.__output._getClass().getPath()}{config.DEFAULT_PLOT_NAME}.png"))
        self.addItemToLayout(self.__label, 2, 1)

        self.__makePlot()


    def __setXName(self, new_x_name: str):
        self.__x_name = new_x_name
        self.__makePlot()

    def __setYName(self, new_y_name: str):
        self.__y_name = new_y_name
        self.__makePlot()

    def __makePlot(self):
        if os.path.exists(f"{config.SIMULATION_PATH}/{self.__output._getClass().getName()}.txt"):
            self.__output._getClass().makePlot(
                self.__x_name,
                self.__y_name,
                f"{config.DEFAULT_PLOT_NAME}",
                self.__output._getClass().getUnits()[self.__output._getClass().getLineNames().index(self.__x_name)],
                self.__output._getClass().getUnits()[self.__output._getClass().getLineNames().index(self.__y_name)],
            )
            self.__label.setPixmap(QtGui.QPixmap(f"{self.__output._getClass().getPath()}{config.DEFAULT_PLOT_NAME}.png"))
