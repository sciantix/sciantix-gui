
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
    file = list(output_file_class)
    
    if (len(file[0].split("\t")) == 5) and output_class.hasSteamPressure()\
            or (len(file[0].split("\t")) == 6) and not output_class.hasSteamPressure():
        output_class.toggleSteamPressure()

    names = output_class.getLineNames()

    for i, line in enumerate(file):
        if i < output_class.getNbrLines():
            for name, val in zip(names, line.split("\t")):
                output_class.setValueByName(f"{i}{name}", eval(val))
        elif output_class.hasSteamPressure():
            time, temperature, fission_rate, hydrostatic_stress, steam_pressure, _ = line.split("\t")
            output_class.addLine(eval(time), eval(temperature), eval(fission_rate), eval(hydrostatic_stress), eval(steam_pressure))
        else:
            time, temperature, fission_rate, hydrostatic_stress, _ = line.split("\t")
            output_class.addLine(eval(time), eval(temperature), eval(fission_rate), eval(hydrostatic_stress))
    