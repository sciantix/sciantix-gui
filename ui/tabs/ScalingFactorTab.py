
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

    Version : 1.3.0
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtWidgets as QtWidgets

from . import Tab


class ScalingFactorTab(Tab.Tab):
    def __init__(self, scaling_factor_class):
        super().__init__("Input Scaling Factor", scaling_factor_class)

        self.__button = QtWidgets.QPushButton(f"Use Scaling Factor : {self._option}")
        self.__button.setStyleSheet("background: darkred")
        self.__button.clicked.connect(self.__toggleOption)
        self.addItemToLayout(self.__button, 0, 1)

        for i, elt in enumerate(self._getClass().getOptionsNames()):
            self.addItemToLayout(QtWidgets.QLabel(elt), i+1, 0)
            current_input = QtWidgets.QLineEdit(str(self._getClass().getValueByName(elt)))
            current_input.textChanged.connect(
                (lambda name:
                    lambda text: self._getClass().setValueByName(name, float(text) if (len(text) != 0) else 0)
                )(elt)
            )
            self.addItemToLayout(current_input, i+1, 1)
    

    def __toggleOption(self):
        self._option = not self._option
        self.__button.setText(f"Use Scaling Factor : {self._option}")
        if self._option:
            self.__button.setStyleSheet("background: green")
        else:
            self.__button.setStyleSheet("background: darkred")
        