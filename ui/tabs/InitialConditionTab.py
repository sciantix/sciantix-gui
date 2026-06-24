
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


import PyQt6.QtWidgets as QtWidgets

from . import Tab


class InitialConditionTab(Tab.Tab):
    def __init__(self, classes):
        super().__init__("Input Initial Condition", classes)
        names = self._class.getOptionsNames()
        i, j  = 0, 0

        for amount in self._class.getLayout():
            k = 0
            for _ in range(amount):
                self.addItemToLayout(QtWidgets.QLabel(names[i]), 2*j, k)
                current_input = QtWidgets.QLineEdit(str(self._class.getValueByName(names[i])))
                current_input.textChanged.connect(
                    (lambda name:
                        lambda text: self._class.setValueByName(name, float(text) if (len(text) != 0) else 0)
                    )(names[i])
                )
                self.addItemToLayout(current_input, 2*j+1, k)
                i += 1
                k += 1

            j += 1
