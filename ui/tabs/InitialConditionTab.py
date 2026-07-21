
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


import PyQt6.QtWidgets as QtWidgets

from . import ScrollableIETab


class InitialConditionTab(ScrollableIETab.ScrollableIETab):
    __slots__ = [
        # From the Tab super-class
        "__name",
        "__class",
        "__layout",
        "_option",
        # From the ScrollableTab super-class
        "__group_box",
        "__scroll",
        
        # From the InitialConditionTab class
        "__value_inputs",
    ]

    def __init__(self, classes):
        super().__init__("Input Initial Condition", classes, box=True)

        self.__value_inputs = []

        names = self._getClass().getOptionsNames()

        line_names = [
            r"",
            r"Xeon (Xe)",
            r"Krypton (Kr)",
            r"Helium (He)",
            r"",
            r"",
            r"",
            r"",
            r"",
            r"Heavy atoms content",
            r"Xe133",
            r"Kr85m",
            r"",
        ]

        displayed_names = [
            r"Grain radius",
            r"Xe produced",
            r"Xe intragranular",
            r"Xe intragranular in solution",
            r"Xe intragranular in bubbles",
            r"Xe grain boundary",
            r"Xe released",
            r"Kr produced",
            r"Kr intragranular",
            r"Kr intragranular in solution",
            r"Kr intragranular in bubbles",
            r"Kr grain boundary",
            r"Kr released",
            r"He produced",
            r"He intragranular",
            r"He intragranular in solution",
            r"He intragranular in bubbles",
            r"He grain boundary",
            r"He released",
            r"Intragranular bubble concentration",
            r"Intragranular bubble radius",
            r"Fuel burn-up",
            r"Fuel effective burn-up",
            r"Irradiation time",
            r"Fuel density",
            r"U234",
            r"U235",
            r"U236",
            r"U237",
            r"U238",
            r"Xe133 produced",
            r"Xe133 intragranular",
            r"Xe133 intragranular in solution",
            r"Xe133 intragranular in bubbles",
            r"Xe133 decayed",
            r"Xe133 grain boundary",
            r"Xe133 released",
            r"Kr85m produced",
            r"Kr85m intragranular",
            r"Kr85m intragranular in solution",
            r"Kr85m intragranular in bubbles",
            r"Kr85m decayed",
            r"Kr85m grain boundary",
            r"Kr85m released",
            r"Fuel stoichiometry deviation",
        ]


        i = 0
        
        for j, amount in enumerate(self._getClass().getLayout()):
            layout = QtWidgets.QGridLayout()
            box    = QtWidgets.QGroupBox()
            box.setLayout(layout)
            self.addItemToLayout(box, j+1, 0)

            gap = 0

            if line_names[j]:
                line_name = QtWidgets.QLabel(line_names[j])
                layout.addWidget(line_name, 0, 1)
                gap += 1

            if self._getClass().getUnits()[j]:
                unit = QtWidgets.QLabel(f"in {self._getClass().getUnits()[j]}")
                if line_names[j]:
                    layout.addWidget(unit, 0, 2)
                else:
                    layout.addWidget(unit, 1, 0)

            for k in range(amount):
                name = QtWidgets.QLabel(displayed_names[i])
                layout.addWidget(name, gap, k+1)
                self.__value_inputs.append(QtWidgets.QLineEdit(str(self._getClass().getValueByName(names[i]))))
                self.__value_inputs[i].textChanged.connect(
                    (lambda name:
                        lambda text: self._getClass().trySetValueByName(name, text)
                    )(names[i])
                )
                layout.addWidget(self.__value_inputs[i], gap+1, k+1)
                i += 1

    def _update_import(self):
        for i, name in enumerate(self._getClass().getOptionsNames()):
            self.__value_inputs[i].setText(str(self._getClass().getValueByName(name)))
