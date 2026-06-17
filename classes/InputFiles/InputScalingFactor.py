
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


class InputScalingFactor(InputFile):
    def __init__(self):
        super().__init__("input_scaling_factor")

        # Base setup
        self.setValueByName("resolution_rate",        1.0)
        self.setValueByName("trapping_rate",          1.0)
        self.setValueByName("nucleation_rate",        1.0)
        self.setValueByName("diffusivity",            1.0)
        self.setValueByName("screw_parameter",        1.0)
        self.setValueByName("span_parameter",         1.0)
        self.setValueByName("cent_parameter",         1.0)
        self.setValueByName("helium_production_rate", 1.0)
        self.setValueByName("dummy",                  1.0)