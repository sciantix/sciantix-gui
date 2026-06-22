
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
        self.addItemToLayout(button, 0, 3)

        self.addItemToLayout(QtWidgets.QLabel("time"),               1, 0)
        self.addItemToLayout(QtWidgets.QLabel("temperature"),        1, 1)
        self.addItemToLayout(QtWidgets.QLabel("fission_rate"),       1, 2)
        self.addItemToLayout(QtWidgets.QLabel("hydrostatic_stress"), 1, 3)

        self.__makeLine()

    
    def __makeLine(self):
        index = self._class.getNbrLines()

        names  = self._class.getLineNames()
        values = self._class.getLineByNbr(index-1)

        for i in range(4):
            current_input = QtWidgets.QLineEdit(str(values[i]))
            current_input.textChanged.connect(
                lambda text: self._class.setValueByName(f"{index-1}{names[i]}", int(text) if (len(text) != 0) else 0)
            )
            self.addItemToLayout(current_input, index+1, i)
    
    def __addLine(self):
        self._class.addLine(0, 0, 0, 0)
        self.__makeLine()
