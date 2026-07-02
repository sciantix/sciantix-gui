
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


import PyQt6.QtWidgets as QtWidgets

from . import Tab


class SettingsTab(Tab.Tab):
    def __init__(self, settings_class):
        super().__init__("Input Settings", settings_class)

        self.__settings_options = [
            ["no grain growth", "Ainscough et al. (1973)", "Van Uffelen et al. (2013)"],
            ["constant value", "Turnbull et al. (1988)"],
            ["SDA with quasi-stationary hypothesis", "SDA without quasi-stationary hypothesis"],
            ["", "Pizzocri et al. (2018)"],
            ["constant value", "Turnbull (1971)", "Losonen (2000)", "thermal resolution", "Cognini et al. (2021)"],
            ["constant value", "Ham (1958)"],
            ["constant value", "Olander, Wongsawaeng (2006)"],
            ["", "default output files"],
            ["constant value", "Reynolds and Burton (1979)", "White (2004)"],
            ["no grain boundary bubbles", "Pastore et al (2013)"],
            ["no model considered", "Barani et al. (2017)"],
            ["UO2", "UO2 + HBS"],
            ["no model considered", "Pizzocri et al., D6.4 (2020), H2020 Project INSPYRE"],
            ["not considered", "considered"],
            ["not considered", "considered"],
            ["null value", "limited lattice damage, Luzzi et al. (2018)", "significant lattice damage, Luzzi et al. (2018)"],
            ["no model considered", "TRANSURANUS swept volume model"],
            ["no model considered", "fraction of HBS-restructured volume from Barani et al. (2020)"],
            ["no evolution of HBS porosity", "HBS porosity evolution based on Spino et al. (2006) data"],
            ["zero production rate", "helium from ternary fissions", "linear with burnup (FR)"],
            ["not considered", "Cox et al. 1986", "Bittel et al. 1969", "Abrefah et al. 1994", "Imamura et al. 1997", "Langmuir-based approach"],
            ["not considered", "volume diffusivity"],

            # iDensification : not used yet 
            # ["not considered", "P. Van Uffelen PhD thesis (2002)"],
        ]

        for i, elt in enumerate(self._class.getOptionsNames()):
            self.addItemToLayout(QtWidgets.QLabel(elt), i, 0)
            current_input = QtWidgets.QComboBox()
            current_input.addItems(self.__settings_options[i])
            current_input.currentIndexChanged.connect(
                (lambda name:
                    lambda index: self._class.setValueByName(name, index)
                )(elt)
            )
            self.addItemToLayout(current_input, i, 1)
        