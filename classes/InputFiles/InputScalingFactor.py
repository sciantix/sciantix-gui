
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
from .. import printable


class InputScalingFactor(InputFile.InputFile, printable.Printable):
    def __init__(self):
        InputFile.InputFile.__init__("input_scaling_factor")
        printable.Printable.__init__(printable.caling_factor_template)

        # Base setup
        self.addOptionInterval("resolution_rate",        1.0, 0, 1e10)
        self.addOptionInterval("trapping_rate",          1.0, 0, 1e10)
        self.addOptionInterval("nucleation_rate",        1.0, 0, 1e10)
        self.addOptionInterval("diffusivity",            1.0, 0, 1e10)
        self.addOptionInterval("screw_parameter",        1.0, 0, 1e10)
        self.addOptionInterval("span_parameter",         1.0, 0, 1e10)
        self.addOptionInterval("cent_parameter",         1.0, 0, 1e10)
        self.addOptionInterval("helium_production_rate", 1.0, 0, 1e10)
        self.addOptionInterval("dummy",                  1.0, 0, 1e10)