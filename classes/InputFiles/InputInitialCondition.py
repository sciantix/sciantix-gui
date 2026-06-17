
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


class InputInitialCondition(InputFile):
    def __init__(self):
        super().__init__("input_initial_condition")

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
        self.setValueByName("grain_radius", 5.0e-06)
        self.setValueByName("Xe_produced",               0.0)
        self.setValueByName("Xe_intragranular",          0.0)
        self.setValueByName("Xe_intragranular_solution", 0.0)
        self.setValueByName("Xe_intragranular_bubbles",  0.0)
        self.setValueByName("Xe_grain_boundary",         0.0)
        self.setValueByName("Xe_released",               0.0)
        self.setValueByName("Kr_produced",               0.0)
        self.setValueByName("Kr_intragranular",          0.0)
        self.setValueByName("Kr_intragranular_solution", 0.0)
        self.setValueByName("Kr_intragranular_bubbles",  0.0)
        self.setValueByName("Kr_grain_boundary",         0.0)
        self.setValueByName("Kr_released",               0.0)
        self.setValueByName("He_produced",               0.0)
        self.setValueByName("He_intragranular",          0.0)
        self.setValueByName("He_intragranular_solution", 0.0)
        self.setValueByName("He_intragranular_bubbles",  0.0)
        self.setValueByName("He_grain_boundary",         0.0)
        self.setValueByName("He_released",               0.0)
        self.setValueByName("intragranular_bubble_concentration", 0.0)
        self.setValueByName("intragranular_bubble_radius",        0.0)
        self.setValueByName("fuel_burn_up", 0.0)
        self.setValueByName("fuel_effective_burn_up", 0.0)
        self.setValueByName("irradiation_time", 0.0)
        self.setValueByName("fuel_density", 10641.0)
        self.setValueByName("U234_content", 0.0)
        self.setValueByName("U235_content", 3.0)
        self.setValueByName("U236_content", 0.0)
        self.setValueByName("U237_content", 0.0)
        self.setValueByName("U238_content", 0.0)
        self.setValueByName("U239_content", 97.0)
        self.setValueByName("Xe133_produced",               0.0)
        self.setValueByName("Xe133_intragranular",          0.0)
        self.setValueByName("Xe133_intragranular_solution", 0.0)
        self.setValueByName("Xe133_intragranular_bubbles",  0.0)
        self.setValueByName("Xe133_decayed",                0.0)
        self.setValueByName("Xe133_grain_boundary",         0.0)
        self.setValueByName("Xe133_released",               0.0)
        self.setValueByName("Kr85m_produced",               0.0)
        self.setValueByName("Kr85m_intragranular",          0.0)
        self.setValueByName("Kr85m_intragranular_solution", 0.0)
        self.setValueByName("Kr85m_intragranular_bubbles",  0.0)
        self.setValueByName("Kr85m_decayed",                0.0)
        self.setValueByName("Kr85m_grain_boundary",         0.0)
        self.setValueByName("Kr85m_released",               0.0)
        self.setValueByName("fuel_stoichiometry",           0.0)


        def getLayout(self) -> list[int]:
            return self.__layout
