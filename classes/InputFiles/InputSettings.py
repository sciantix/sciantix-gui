
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


from . import InputFile


class InputSettings(InputFile):
    def __init__(self):
        super().__init__("input_settings")

        # Base setup
        self.setValueByName("iGrainGrowth",                     1)
        self.setValueByName("iFissionGasDiffusivity",           1)
        self.setValueByName("iDiffusionSolver",                 1)
        self.setValueByName("iIntraGranularBubbleBehavior",     1)
        self.setValueByName("iResolutionRate",                  1)
        self.setValueByName("iTrappingRate",                    1)
        self.setValueByName("iNucleationRate",                  1)
        self.setValueByName("iOutput",                          1)
        self.setValueByName("iGrainBoundaryVacancyDiffusivity", 1)
        self.setValueByName("iGrainBoundaryBehaviour",          1)
        self.setValueByName("iGrainBoundaryMicroCracking",      1)
        self.setValueByName("iFuelMatrix",                      0)
        self.setValueByName("iGrainBoundaryVenting",            0)
        self.setValueByName("iRadioactiveFissionGas",           0)
        self.setValueByName("iHelium",                          0)
        self.setValueByName("iHeDiffusivity",                   0)
        self.setValueByName("iGrainBoundarySweeping",           0)
        self.setValueByName("iHighBurnupStructureFormation",    0)
        self.setValueByName("iHighBurnupStructurePorosity",     0)
        self.setValueByName("iHeliumProductionRate",            0)
        self.setValueByName("iStoichiometryDeviation",          0)
        self.setValueByName("iBubbleDiffusivity",               0)