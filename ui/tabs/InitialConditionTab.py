
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

    Version : 1.4.0
    Year :    2026
    Authors : G. Léandre
"""


import PyQt6.QtWidgets as QtWidgets

from . import Tab


class InitialConditionTab(Tab.Tab):
    def __init__(self, classes):
        super().__init__("Input Initial Condition", classes)
        names = self._getClass().getOptionsNames()
        i     = 0

        for j, amount in enumerate(self._getClass().getLayout()):
            if self._getClass().getUnits():
                self.addItemToLayout(QtWidgets.QLabel(f"in {self._getClass().getUnits()[j]}"), 2*j+1, 0)
    
            for k in range(amount):
                self.addItemToLayout(QtWidgets.QLabel(names[i]), 2*j, k+1)
                current_input = QtWidgets.QLineEdit(str(self._getClass().getValueByName(names[i])))
                current_input.textChanged.connect(
                    (lambda name:
                        lambda text: self._getClass().setValueByName(name, float(text) if (len(text) != 0) else 0)
                    )(names[i])
                )
                self.addItemToLayout(current_input, 2*j+1, k+1)
                i += 1
