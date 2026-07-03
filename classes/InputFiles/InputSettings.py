
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


from . import InputFile
from .. import config
from .. import FileAccess


class InputSettings(InputFile.InputFile, FileAccess.Printable):
    def __init__(self):
        InputFile.InputFile.__init__(self, "input_settings")
        FileAccess.Printable.__init__(self, FileAccess.settings_template)

        # Base setup
        self.addOptionSet("GrainGrowth",                     config.SETTINGS_DEFAULT, (0, 1, 2))
        self.addOptionSet("FissionGasDiffusivity",           config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("DiffusionSolver",                 config.SETTINGS_DEFAULT, (0, 1, 2))
        self.addOptionSet("IntraGranularBubbleBehavior",     config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("ResolutionRate",                  config.SETTINGS_DEFAULT, (0, 1, 2, 3))
        self.addOptionSet("TrappingRate",                    config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("NucleationRate",                  config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("Output",                          config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("GrainBoundaryVacancyDiffusivity", config.SETTINGS_DEFAULT, (0, 1, 2))
        self.addOptionSet("GrainBoundaryBehaviour",          config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("GrainBoundaryMicroCracking",      config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("FuelMatrix",                      config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("GrainBoundaryVenting",            config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("RadioactiveFissionGas",           config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("Helium",                          config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("HeDiffusivity",                   config.SETTINGS_DEFAULT, (0, 1, 2))
        self.addOptionSet("GrainBoundarySweeping",           config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("HighBurnupStructureFormation",    config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("HighBurnupStructurePorosity",     config.SETTINGS_DEFAULT, (0, 1))
        self.addOptionSet("HeliumProductionRate",            config.SETTINGS_DEFAULT, (0, 1, 2))
        self.addOptionSet("StoichiometryDeviation",          config.SETTINGS_DEFAULT, (0, 1, 2, 3, 4, 5))
        self.addOptionSet("BubbleDiffusivity",               config.SETTINGS_DEFAULT, (0, 1))
        