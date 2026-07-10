
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

    Version : 1.4.0
    Year :    2026
    Authors : G. Léandre
"""

from .. import FileAccess
from ..InputFiles import InputFile, MultiLines


# For this class, the options names (which serves as keys) are precede by the line index
# For Exemple :
#       0time
# Is the time value for the 1st line

class OutputFile(InputFile.InputFile, MultiLines.MultiLines, FileAccess.Readable, FileAccess.Plotable):
    def __init__(self):
        InputFile.InputFile.__init__(self, "output")
        MultiLines.MultiLines.__init__(self)
        FileAccess.Readable.__init__(self)
        FileAccess.Plotable.__init__(self)

        self.__column_names = [
            "time",
            "temperature",
            "fission_rate",
            "hydrostatic_stress",
            "grain_radius",
            "Xe_produced",
            "Xe_grain",
            "Xe_intragranular_solution",
            "Xe_intragranular_bubbles",
            "Xe_grain_boundary",
            "Xe_released",
            "Kr_produced",
            "Kr_grain",
            "Kr_intragranular_solution",
            "Kr_intragranular_bubbles",
            "Kr_grain_boundary",
            "Kr_released",
            "fission_gas_release",
            "intragranular_bubble_concentration",
            "intragranular_bubble_radius",
            "intragranular_gas_bubble_swelling",
            "intergranular_bubble_concentration",
            "intergranular_atoms_bubble",
            "intergranular_vacancies_bubble",
            "intergranular_bubble_radius",
            "intergranular_bubble_area",
            "intergranular_bubble_volume",
            "intergranular_fractional_coverage",
            "intergranular_saturation_fractional_coverage",
            "intergranular_gas_swelling",
            "intergranular_fractional_intactness",
            "burnup",
            "U235",
            "U238",
        ]

        self.__units = [
            "h",
            "K",
            "fiss/m3s",
            "MPa",
            "m",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "at/m3",
            "",
            "bub/m3",
            "m",
            "",
            "bub/m2",
            "at/bub",
            "vac/bub",
            "m",
            "m2",
            "m3",
            "",
            "",
            "",
            "",
            "MWd/kg",
            "at/m3",
            "at/m3",
        ]
    

    def __checkIsnumber(self, string: str) -> bool:
        """
        check if string can be is a number convertible into a float
        """
        splits = string.strip().split('e')

        ans = 1 <= len(splits) <= 2

        for i in range(len(splits)):
            if ans and len(splits[i]) and splits[i][0] in "+-":
                splits[i] = splits[i][1:]
            
            ans = ans and splits[i].replace('.', '', 1).isnumeric()

        return ans
    
    def getUnits(self) -> list[str]:
        return self.__units

    def getLineNames(self) -> tuple:
        return tuple(self.__column_names)

    def getLineByNbr(self, index: int) -> tuple:
        if not (0 <= index < self.getNbrLines()):
            raise IndexError("You can't get a line that doesn't exist, index must be between 0 and InputHistory.getNbrLines()")

        return tuple(
            self.getValueByName(f"{index}{name}")
            for name in self.__column_names
        )
    
    def addLine(self, *args):
        values = list(*args)
        for i in range(len(self.__column_names)):
            if i < len(values) and self.__checkIsnumber(values[i]):
                self.addOptionOutput(f"{self.getNbrLines()}{self.__column_names[i]}", float(values[i]))
            else:
                self.addOptionOutput(f"{self.getNbrLines()}{self.__column_names[i]}", 0)

        self._incrementLineNbr()
    
    def deleteLineByNbr(self, index: int):
        # Not Implemented yet and probably wont be since I don't think it's needed for now
        pass
