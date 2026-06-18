
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


class InputInitialCondition(InputFile.InputFile, printable.Printable):
    def __init__(self):
        InputFile.InputFile.__init__(self, "input_initial_condition")
        printable.Printable.__init__(self, printable.initial_condition_template)

        # Variable to represent the layout of data from the input_initial_condition.txt input file
        # Each element of the array represent the number of factor on each lines of input_initial_condition.txt
        self.__layout = [
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

        # Base setup
        self.addOptionInterval("grain_radius", 5.0e-06, 0, 1e10)
        self.addOptionInterval("Xe_produced",               0.0, 0, 1e10)
        self.addOptionInterval("Xe_intragranular",          0.0, 0, 1e10)
        self.addOptionInterval("Xe_intragranular_solution", 0.0, 0, 1e10)
        self.addOptionInterval("Xe_intragranular_bubbles",  0.0, 0, 1e10)
        self.addOptionInterval("Xe_grain_boundary",         0.0, 0, 1e10)
        self.addOptionInterval("Xe_released",               0.0, 0, 1e10)
        self.addOptionInterval("Kr_produced",               0.0, 0, 1e10)
        self.addOptionInterval("Kr_intragranular",          0.0, 0, 1e10)
        self.addOptionInterval("Kr_intragranular_solution", 0.0, 0, 1e10)
        self.addOptionInterval("Kr_intragranular_bubbles",  0.0, 0, 1e10)
        self.addOptionInterval("Kr_grain_boundary",         0.0, 0, 1e10)
        self.addOptionInterval("Kr_released",               0.0, 0, 1e10)
        self.addOptionInterval("He_produced",               0.0, 0, 1e10)
        self.addOptionInterval("He_intragranular",          0.0, 0, 1e10)
        self.addOptionInterval("He_intragranular_solution", 0.0, 0, 1e10)
        self.addOptionInterval("He_intragranular_bubbles",  0.0, 0, 1e10)
        self.addOptionInterval("He_grain_boundary",         0.0, 0, 1e10)
        self.addOptionInterval("He_released",               0.0, 0, 1e10)
        self.addOptionInterval("intragranular_bubble_concentration", 0.0, 0, 1e10)
        self.addOptionInterval("intragranular_bubble_radius",        0.0, 0, 1e10)
        self.addOptionInterval("fuel_burn_up", 0.0, 0, 1e10)
        self.addOptionInterval("fuel_effective_burn_up", 0.0, 0, 1e10)
        self.addOptionInterval("irradiation_time", 0.0, 0, 1e10)
        self.addOptionInterval("fuel_density", 10641.0, 0, 1e10)
        self.addOptionInterval("U234_content", 0.0, 0, 1e10)
        self.addOptionInterval("U235_content", 3.0, 0, 1e10)
        self.addOptionInterval("U236_content", 0.0, 0, 1e10)
        self.addOptionInterval("U237_content", 0.0, 0, 1e10)
        self.addOptionInterval("U238_content", 0.0, 0, 1e10)
        self.addOptionInterval("U239_content", 97.0, 0, 1e10)
        self.addOptionInterval("Xe133_produced",               0.0, 0, 1e10)
        self.addOptionInterval("Xe133_intragranular",          0.0, 0, 1e10)
        self.addOptionInterval("Xe133_intragranular_solution", 0.0, 0, 1e10)
        self.addOptionInterval("Xe133_intragranular_bubbles",  0.0, 0, 1e10)
        self.addOptionInterval("Xe133_decayed",                0.0, 0, 1e10)
        self.addOptionInterval("Xe133_grain_boundary",         0.0, 0, 1e10)
        self.addOptionInterval("Xe133_released",               0.0, 0, 1e10)
        self.addOptionInterval("Kr85m_produced",               0.0, 0, 1e10)
        self.addOptionInterval("Kr85m_intragranular",          0.0, 0, 1e10)
        self.addOptionInterval("Kr85m_intragranular_solution", 0.0, 0, 1e10)
        self.addOptionInterval("Kr85m_intragranular_bubbles",  0.0, 0, 1e10)
        self.addOptionInterval("Kr85m_decayed",                0.0, 0, 1e10)
        self.addOptionInterval("Kr85m_grain_boundary",         0.0, 0, 1e10)
        self.addOptionInterval("Kr85m_released",               0.0, 0, 1e10)
        self.addOptionInterval("fuel_stoichiometry",           0.0, 0, 1e10)


    def getLayout(self) -> list[int]:
        return self.__layout
