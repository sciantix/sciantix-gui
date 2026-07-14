
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

    Version : 1.5.0
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtWidgets as QtWidgets

from . import Tab


class ScalingFactorTab(Tab.Tab):
    def __init__(self, scaling_factor_class):
        super().__init__("Input Scaling Factor", scaling_factor_class)

        self._option = False

        self.__button = QtWidgets.QPushButton(f"Use Scaling Factor : {self._option}")
        self.__updateState()
        self.__button.clicked.connect(self.__toggleOption)
        self.addItemToLayout(self.__button, 0, 1)

        for i, elt in enumerate(self._getClass().getOptionsNames()):
            self.addItemToLayout(QtWidgets.QLabel(self._pretifyText(elt)), i+1, 0)
            current_input = QtWidgets.QLineEdit(str(self._getClass().getValueByName(elt)))
            current_input.textChanged.connect(
                (lambda name:
                    lambda text: self._getClass().trySetValueByName(name, text)
                )(elt)
            )
            self.addItemToLayout(current_input, i+1, 1)
    

    def __toggleOption(self):
        self._option = not self._option
        self.__button.setText(f"Use Scaling Factor : {self._option}")
        self.__updateState()

    def __updateState(self):
        # To have the button and its state unically identifyable in the stylesheet
        self.__button.setProperty("state", "True" if self._option else "False")
        # To counter PyQt's caching and have the style updated
        self.__button.style().unpolish(self.__button)
        self.__button.style().polish(self.__button)
        