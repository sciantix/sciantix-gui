
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

    Version : 1.2.0
    Year :    2026
    Authors : G. Léandre
"""

import os
import PyQt6.QtWidgets as QtWidgets

from . import ScrollableTab


class OutputTab(ScrollableTab.ScrollableTab):
    def __init__(self, output_class):
        super().__init__("Output", output_class)

        self._option = False

        for i, name in enumerate(self._class.getLineNames()):
            self.addItemToLayout(QtWidgets.QLabel(name), 0, i)
        
    
    def __make_layout(self):
        for line in range(self._class.getNbrLines()):
            for column, value in enumerate(self._class.getLineByNbr(line)):
                self.addItemToLayout(QtWidgets.QLabel(str(value)), line, column)
    
    def read(self):
        if os.path.exists(f"sciantix/{self._class.getName()}.txt"):
            self._class.read()

        self.__make_layout()    
        