
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


from . import InputFile
from .. import config
from .. import FileAccess


class InputInitialCondition(InputFile.InputFile, FileAccess.Printable, FileAccess.Readable):
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

        # From the InputInitialCondition class
        "__layout",
        "__units"
    ]

    def __init__(self):
        InputFile.InputFile.__init__(self, "input_initial_conditions")
        FileAccess.Printable.__init__(self, FileAccess.initial_condition_print_template)
        FileAccess.Readable.__init__(self, FileAccess.initial_condition_read_template)

        # Variable to represent the layout of data from the input_initial_condition.txt input file
        # Each element of the array represent the number of factor on each lines of input_initial_condition.txt
        self.__layout = config.INITIAL_CONDITION_LAYOUT
        self.__units  = config.INITIAL_CONDITION_UNITS

        # TODO : Maybe clean up by putting the initial conditions into config.py
        # Base setup
        self.addOptionInterval("grain_radius", 5.0e-06, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe_produced",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe_intragranular",          0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe_intragranular_solution", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe_intragranular_bubbles",  0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe_grain_boundary",         0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe_released",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr_produced",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr_intragranular",          0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr_intragranular_solution", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr_intragranular_bubbles",  0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr_grain_boundary",         0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr_released",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("He_produced",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("He_intragranular",          0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("He_intragranular_solution", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("He_intragranular_bubbles",  0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("He_grain_boundary",         0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("He_released",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("intragranular_bubble_concentration", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("intragranular_bubble_radius",        0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("fuel_burn_up", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("fuel_effective_burn_up", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("irradiation_time", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("fuel_density", 10641.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("U234_content", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("U235_content", 3.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("U236_content", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("U237_content", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("U238_content", 97.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe133_produced",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe133_intragranular",          0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe133_intragranular_solution", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe133_intragranular_bubbles",  0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe133_decayed",                0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe133_grain_boundary",         0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Xe133_released",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr85m_produced",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr85m_intragranular",          0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr85m_intragranular_solution", 0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr85m_intragranular_bubbles",  0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr85m_decayed",                0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr85m_grain_boundary",         0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("Kr85m_released",               0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)
        self.addOptionInterval("fuel_stoichiometry",           0.0, config.INITIAL_CONDITION_LOWER_BOUND, config.INITIAL_CONDITION_UPER_BOUND)


    def getLayout(self) -> list[int]:
        return self.__layout
    
    def getUnits(self) -> list[str]:
        return self.__units
