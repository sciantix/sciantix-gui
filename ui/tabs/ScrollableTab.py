
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

    Version : 1.4.0
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtCore    as QtCore
import PyQt6.QtWidgets as QtWidgets

from . import Tab


class ScrollableTab(Tab.Tab):
    def __init__(self, name: str, classe):
        super().__init__(name, classe)

        self.__group_box = QtWidgets.QGroupBox()
        self.__group_box.setLayout(self._getLayout())

        self.__scroll = QtWidgets.QScrollArea()
        self.__scroll.setWidget(self.__group_box)
        self.__scroll.setWidgetResizable(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.__scroll)
