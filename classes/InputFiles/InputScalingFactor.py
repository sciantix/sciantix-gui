
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


from . import InputFile
from .. import config
from .. import printable


class InputScalingFactor(InputFile.InputFile, printable.Printable):
    def __init__(self):
        InputFile.InputFile.__init__(self, "input_scaling_factor")
        printable.Printable.__init__(self, printable.scaling_factor_template)

        # Base setup
        self.addOptionInterval("resolution_rate",        config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("trapping_rate",          config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("nucleation_rate",        config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("diffusivity",            config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("screw_parameter",        config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("span_parameter",         config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("cent_parameter",         config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("helium_production_rate", config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
        self.addOptionInterval("dummy",                  config.SCALING_FACTOR_DEFAULT, config.SCALING_FACTOR_LOWER_BOUND, config.SCALING_FACTOR_UPER_BOUND)
