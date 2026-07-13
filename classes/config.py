
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

    Version : 1.4.2
    Year :    2026
    Authors : G. Léandre
"""


# +--------------------------------+
# |   Input Files Classes config   |
# +--------------------------------+

# InputScalingFactor
SETTINGS_DEFAULT = 0

# InputHistory
HISTORY_LOWER_BOUND = -1e21
HISTORY_UPER_BOUND  =  1e20
HISTORY_UNITS = [
    r"h",
    r"K",
    r"fiss/m3s",
    r"MPa",
    r"",
]

# InputInitialCondition
INITIAL_CONDITION_LAYOUT = [
    1,
    6,
    6,
    6,
    2,
    1,
    1,
    1,
    1,
    5,
    7,
    7,
    1
]
INITIAL_CONDITION_UNITS = [
    r"m",
    r"at/m3",
    r"at/m3",
    r"at/m3",
    r"at/m3",
    r"MWd/kgUO2",
    r"MWd/kgUO2",
    r"h",
    r"kg/m3",
    r"%",
    r"at/m3",
    r"at/m3",
    r""
]
INITIAL_CONDITION_LOWER_BOUND = -1e10
INITIAL_CONDITION_UPER_BOUND  =  1e10

# InputScalingFactor
SCALING_FACTOR_DEFAULT     = 1.0
SCALING_FACTOR_LOWER_BOUND = -1e10
SCALING_FACTOR_UPER_BOUND  =  1e10
