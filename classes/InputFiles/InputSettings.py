
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


from . import InputFile
from .. import config
from .. import FileAccess


class InputSettings(InputFile.InputFile, FileAccess.Printable, FileAccess.Readable):
    __slots__ = [
        # From the InputFile super-class
        "__options",
        "__name",

        # From the FileAccess super-interface
        "__path",
        # From the Printable interface
        "__print_template"
        # From the Readable interface
        "__read_template"
        
        # From the InputSettings class
    ]

    def __init__(self):
        InputFile.InputFile.__init__(self, "input_settings")
        FileAccess.Printable.__init__(self, FileAccess.settings_print_template)
        FileAccess.Readable.__init__(self, FileAccess.settings_read_template)

        # Base setup
        self.addOptionSet("GrainGrowth",                     1,                       (0, 1, 2))
        self.addOptionSet("FissionGasDiffusivity",           1,                       (0, 1))
        self.addOptionSet("DiffusionSolver",                 1,                       (1, 2))
        self.addOptionSet("IntraGranularBubbleBehavior",     1,                       [1])
        self.addOptionSet("ResolutionRate",                  1,                       (0, 1, 2, 3))
        self.addOptionSet("TrappingRate",                    1,                       (0, 1))
        self.addOptionSet("NucleationRate",                  1,                       (0, 1))
        self.addOptionSet("Output",                          1,                       [1])
        self.addOptionSet("GrainBoundaryVacancyDiffusivity", 1,                       (0, 1, 2))
        self.addOptionSet("GrainBoundaryBehaviour",          1,                       (0, 1))
        self.addOptionSet("GrainBoundaryMicroCracking",      1,                       (0, 1))
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
        self.addOptionSet("Densification",                   config.SETTINGS_DEFAULT, (0, 1))
        