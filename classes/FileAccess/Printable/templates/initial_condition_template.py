
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


def template(input_file_class):
    file_content = str()
    i, j         = 0, 0
    data         = input_file_class.getOptionsNames()

    comments = [
        r"initial grain radius (m)",
        r"initial Xe (at/m3) produced, intragranular, intragranular in solution, intragranular in bubbles, grain boundary, released",
        r"initial Kr (at/m3) produced, intragranular, intragranular in solution, intragranular in bubbles, grain boundary, released",
        r"initial He (at/m3) produced, intragranular, intragranular in solution, intragranular in bubbles, grain boundary, released",
        r"initial intragranular bubble concentration (at/m3), radius (m)",
        r"initial fuel burn-up (MWd/kgUO2)",
        r"initial fuel effective burn-up (MWd/kgUO2)",
        r"initial irradiation time (h)",
        r"initial fuel density (kg/m3)",
        r"initial U234 U235 U236 U237 U238 (% of heavy atoms) content",
        r"initial Xe133 (at/m3) produced, intragranular, intragranular in solution, intragranular in bubbles, decayed, grain boundary, released",
        r"initial Kr85m (at/m3) produced, intragranular, intragranular in solution, intragranular in bubbles, decayed, grain boundary, released",
        r"initial fuel stoichiometry deviation (\)",
    ]

    
    for amount in input_file_class.getLayout():
        for _ in range(amount):
            file_content += f"{input_file_class.getValueByName(data[i])} "
            i += 1

        file_content += f"\n#\t{comments[j]}\n"
        j += 1

    return file_content
