
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
import PyQt6.QtWidgets as QtWidgets

from . import ScrollableIETab
from .. import config


class OutputTab(ScrollableIETab.ScrollableIETab):
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
        
        "__column_box_layouts",
    ]

    def __init__(self, output_class):
        super().__init__("Output", output_class)

        self.__column_box_layouts = []
        
        for i, name in enumerate(self._getClass().getLineNames()):
            layout = QtWidgets.QGridLayout()
            box    = QtWidgets.QGroupBox()
            box.setLayout(layout)
            self.__column_box_layouts.append(layout)
            self.addItemToLayout(box, 1, i)

            if self._getClass().getUnits():
                label = QtWidgets.QLabel(f"{self._pretifyText(name)} in {self._getClass().getUnits()[i]}")
            else:
                label = QtWidgets.QLabel(self._pretifyText(name))
                
            layout.addWidget(label, 1, 0)
        
    
    def __make_layout(self):
        for line in range(self._getClass().getNbrLines()):
            for column, value in enumerate(self._getClass().getLineByNbr(line)):
                label = QtWidgets.QLabel(str(value))
                self.__column_box_layouts[column].addWidget(label, line+2, 0)

    
    def read(self):
        if os.path.exists(f"{config.SIMULATION_PATH}/{self._getClass().getName()}.txt"):
            self._getClass().read()

        self.__make_layout()

    def _update_import(self):
        self.__make_layout()
        