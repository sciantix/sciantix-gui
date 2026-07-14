
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

import numpy
import matplotlib.pyplot as plt

from .. import FileAccess


# For this class, the options names (which serves as keys) are precede by the line index
# For Exemple :
#       0time
# Is the time value for the 1st line

class Plotable(FileAccess.FileAccess):
    def __init__(self):
        super().__init__()


    def __getArrayByName(self, name: str):
        """
        return all the values from the column of specified name in the form of a numpy array
        """
        if name not in self.getLineNames():
            raise KeyError("You can't get this column : this name doesn't exist")

        return numpy.array([
            self.getValueByName(f"{i}{name}")
            for i in range(self.getNbrLines())
        ])
    
    def makePlot(self, x_name: str, y_name: str, plot_name: str = "plot", x_unit: str = "", y_unit: str = ""):
        x_array = self.__getArrayByName(x_name)
        y_array = self.__getArrayByName(y_name)

        fig, ax = plt.subplots()
        ax.plot(x_array, y_array)

        ax.set_title(f"{y_name} in function of {x_name}")

        if len(x_unit) != 0:
            ax.set_xlabel(f"{x_name} in {x_unit}")
        else:
            ax.set_xlabel(x_name)

        if len(y_unit) != 0:
            ax.set_ylabel(f"{y_name} in {y_unit}")
        else:
            ax.set_ylabel(y_name)


        fig.savefig(f"{self.getPath()}{plot_name}.png")
