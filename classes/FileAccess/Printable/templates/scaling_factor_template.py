
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

    Version : 1.4.0
    Year :    2026
    Authors : G. Léandre
"""


def template(input_file_class):
    file_content = str()
    i            = 0

    comments = [
        r"scaling factor - resolution rate",
        r"scaling factor - trapping rate",
        r"scaling factor - nucleation rate",
        r"scaling factor - diffusivity",
        r"scaling factor - screw parameter",
        r"scaling factor - span parameter",
        r"scaling factor - cent parameter",
        r"scaling factor - helium production rate",
        r"scaling factor - dummy",
    ]


    for name in input_file_class.getOptionsNames():
        file_content += f"{input_file_class.getValueByName(name)}\n# {comments[i]}\n"
        i += 1

    return file_content
