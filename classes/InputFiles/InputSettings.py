
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


class InputSettings(InputFile.InputFile):
    def __init__(self):
        super().__init__("input_settings")

        # Base setup
        self.addOptionSet("GrainGrowth",                     1, (0, 1, 2))
        self.addOptionSet("FissionGasDiffusivity",           1, (0, 1))
        self.addOptionSet("DiffusionSolver",                 1, (0, 1, 2))
        self.addOptionSet("IntraGranularBubbleBehavior",     1, (0, 1))
        self.addOptionSet("ResolutionRate",                  1, (0, 1, 2, 3))
        self.addOptionSet("TrappingRate",                    1, (0, 1))
        self.addOptionSet("NucleationRate",                  1, (0, 1))
        self.addOptionSet("Output",                          1, (0, 1))
        self.addOptionSet("GrainBoundaryVacancyDiffusivity", 1, (0, 1, 2))
        self.addOptionSet("GrainBoundaryBehaviour",          1, (0, 1))
        self.addOptionSet("GrainBoundaryMicroCracking",      1, (0, 1))
        self.addOptionSet("FuelMatrix",                      0, (0, 1))
        self.addOptionSet("GrainBoundaryVenting",            0, (0, 1))
        self.addOptionSet("RadioactiveFissionGas",           0, (0, 1))
        self.addOptionSet("Helium",                          0, (0, 1))
        self.addOptionSet("HeDiffusivity",                   0, (0, 1, 2))
        self.addOptionSet("GrainBoundarySweeping",           0, (0, 1))
        self.addOptionSet("HighBurnupStructureFormation",    0, (0, 1))
        self.addOptionSet("HighBurnupStructurePorosity",     0, (0, 1))
        self.addOptionSet("HeliumProductionRate",            0, (0, 1, 2))
        self.addOptionSet("StoichiometryDeviation",          0, (0, 1, 2, 3, 4, 5))
        self.addOptionSet("BubbleDiffusivity",               0, (0, 1))
        