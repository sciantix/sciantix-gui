
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

        # False for linear, True for logarithmic
        self.__axis_type = { "x": False, "y": False }


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
    
    def __makePlot(self, x_name: str, y_name: str, x_unit: str = "", y_unit: str = ""):
        x_array = self.__getArrayByName(x_name)
        y_array = self.__getArrayByName(y_name)

        fig, ax = plt.subplots()
        ax.plot(x_array, y_array)

        ax.set_title(f"{y_name} in function of {x_name}")

        if self.__axis_type["x"]:
            ax.set_xscale("log")
        else:
            ax.set_xscale("linear")

        if self.__axis_type["y"]:
            ax.set_yscale("log")
        else:
            ax.set_yscale("linear")

        if len(x_unit) != 0:
            ax.set_xlabel(f"{x_name} in {x_unit}")
        else:
            ax.set_xlabel(x_name)

        if len(y_unit) != 0:
            ax.set_ylabel(f"{y_name} in {y_unit}")
        else:
            ax.set_ylabel(y_name)

        return fig

    def setXAxisType(self, new_type: str):
        """
        set the axis scale : 
            new_type = `lin`, for a linear scale
            new_type = `log`, for a logarithmic scale
        """
        self.__axis_type["x"] = new_type == "log"

    def setYAxisType(self, new_type: str):
        """
        set the axis scale : 
            new_type = `lin`, for a linear scale
            new_type = `log`, for a logarithmic scale
        """
        self.__axis_type["y"] = new_type == "log"

    def makePlot(self, x_name: str, y_name: str, plot_name: str = "plot", x_unit: str = "", y_unit: str = ""):
        fig = self.__makePlot(x_name, y_name, x_unit, y_unit)

        fig.savefig(f"{self.getPath()}{plot_name}.png")
        plt.close()
    
    def export(self, file_path: str, x_name: str, y_name: str, x_unit: str = "", y_unit: str = ""):
        fig = self.__makePlot(x_name, y_name, x_unit, y_unit)

        fig.savefig(f"{file_path}/{y_name}_in_function_of_{x_name}.png")
        plt.close()
