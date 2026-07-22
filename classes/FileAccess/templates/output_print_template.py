
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


def template(output_class, output_file_class):
    for i, line in enumerate(output_file_class):
        if i != 0:
            output_class.addLine(line.split("\t"))
    
def template(input_file_class):
    file_content = "Time (h)	Temperature (K)	Fission rate (fiss / m3 s)	Hydrostatic stress (MPa)	Grain radius (m)	Xe produced (at/m3)	Xe in grain (at/m3)	Xe in intragranular solution (at/m3)	Xe in intragranular bubbles (at/m3)	Xe at grain boundary (at/m3)	Xe released (at/m3)	Kr produced (at/m3)	Kr in grain (at/m3)	Kr in intragranular solution (at/m3)	Kr in intragranular bubbles (at/m3)	Kr at grain boundary (at/m3)	Kr released (at/m3)	Fission gas release (/)	Intragranular bubble concentration (bub/m3)	Intragranular bubble radius (m)	Intragranular gas bubble swelling (/)	Intergranular bubble concentration (bub/m2)	Intergranular atoms per bubble (at/bub)	Intergranular vacancies per bubble (vac/bub)	Intergranular bubble radius (m)	Intergranular bubble area (m2)	Intergranular bubble volume (m3)	Intergranular fractional coverage (/)	Intergranular saturation fractional coverage (/)	Intergranular gas swelling (/)	Intergranular fractional intactness (/)	Burnup (MWd/kgUO2)	U235 (at/m3)	U238 (at/m3)	\n"
    
    for i in range(input_file_class.getNbrLines()):
        for elt in input_file_class.getLineByNbr(i):
            file_content += f"{elt}\t"

        file_content += '\n'

    return file_content