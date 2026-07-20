
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


def template(output_class, output_file_class):
    j = 0

    names = [
        "grain_radius",
        "Xe_produced",
        "Xe_intragranular",
        "Xe_intragranular_solution",
        "Xe_intragranular_bubbles",
        "Xe_grain_boundary",
        "Xe_released",
        "Kr_produced",
        "Kr_intragranular",
        "Kr_intragranular_solution",
        "Kr_intragranular_bubbles",
        "Kr_grain_boundary",
        "Kr_released",
        "He_produced",
        "He_intragranular",
        "He_intragranular_solution",
        "He_intragranular_bubbles",
        "He_grain_boundary",
        "He_released",
        "intragranular_bubble_concentration",
        "intragranular_bubble_radius",
        "fuel_burn_up",
        "fuel_effective_burn_up",
        "irradiation_time",
        "fuel_density",
        "U234_content",
        "U235_content",
        "U236_content",
        "U237_content",
        "U238_content",
        "Xe133_produced",
        "Xe133_intragranular",
        "Xe133_intragranular_solution",
        "Xe133_intragranular_bubbles",
        "Xe133_decayed",
        "Xe133_grain_boundary",
        "Xe133_released",
        "Kr85m_produced",
        "Kr85m_intragranular",
        "Kr85m_intragranular_solution",
        "Kr85m_intragranular_bubbles",
        "Kr85m_decayed",
        "Kr85m_grain_boundary",
        "Kr85m_released",
        "fuel_stoichiometry",
    ]

    for i, line in enumerate(output_file_class):
        if not i%2:
            for val in line.strip().split(" "):
                output_class.setValueByName(names[j], eval(val))
                j += 1

