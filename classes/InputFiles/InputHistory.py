
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


# For this class, the options names (which serves as keys) are precede by the line index
# For Exemple :
#       0time
# Is the time value for the 1st line

class InputHistory(InputFile.InputFile, printable.Printable):
    def __init__(self, has_steam_pressure: bool = False):
        InputFile.InputFile.__init__("input_history")
        printable.Printable.__init__(printable.history_template)

        self.__nbr_lines          = 1
        self.__has_steam_pressure = has_steam_pressure

        # Base setup : seting up the first line
        self.addOptionInterval("0time",               0,    0, 1e20)
        self.addOptionInterval("0temperature",        1273, 0, 1e20)
        self.addOptionInterval("0fission_rate",       1e19, 0, 1e20)
        self.addOptionInterval("0hydrostatic_stress", 0,    0, 1e20)

        if has_steam_pressure is not None:
            self.addOptionInterval("0steam_pressure", 0, 0, 1e20)

    
    def getNbrLines(self) -> int:
        return self.__nbr_lines
    
    def getLineByNbr(self, index: int) -> tuple:
        """
        Return the lines values as a tuple of 4 or 5 elements depending on the has_steam_pressure flag

        The order is :
            (time, temperature, fission rate, hydrostatic stress)
                                    or
            (time, temperature, fission rate, hydrostatic stress, steam pressure)
        """
        if not (0 <= index < self.__nbr_lines):
            raise IndexError
        
        if self.__has_steam_pressure:
            line = (
                self.getValueByName(f"{index}time"),
                self.getValueByName(f"{index}temperature"),
                self.getValueByName(f"{index}fission_rate"),
                self.getValueByName(f"{index}hydrostatic_stress"),
                self.getValueByName(f"{index}steam_pressure"),
            )
        else:
            line = (
                self.getValueByName(f"{index}time"),
                self.getValueByName(f"{index}temperature"),
                self.getValueByName(f"{index}fission_rate"),
                self.getValueByName(f"{index}hydrostatic_stress"),
            )

        return line
    
    def addLine(self, time: int, temperature: int, fission_rate: int, hydrostatic_stress: int, steam_pressure: int | None = None):
        if steam_pressure is None and self.__has_steam_pressure:
            raise TypeError

        self.addOptionInterval(f"{self.__nbr_lines}time", time,                             0, 1e20)
        self.addOptionInterval(f"{self.__nbr_lines}temperature", temperature,               0, 1e20)
        self.addOptionInterval(f"{self.__nbr_lines}fission_rate", fission_rate,             0, 1e20)
        self.addOptionInterval(f"{self.__nbr_lines}hydrostatic_stress", hydrostatic_stress, 0, 1e20)

        if steam_pressure is not None:
            self.addOptionInterval(f"{self.__nbr_lines}steam_pressure", steam_pressure, 0, 1e20)

        self.__nbr_lines += 1


# Maybe on a future version, but would require to modify the InputFile base class

#    def deleteLine(self, index: int):
#        if not (0 <= index < self.__nbr_lines):
#            raise IndexError
#        
#        self.setValueByName(f"{self.__nbr_lines}time", time)
#        self.setValueByName(f"{self.__nbr_lines}temperature", temperature)
#        self.setValueByName(f"{self.__nbr_lines}fission_rate", fission_rate)
#        self.setValueByName(f"{self.__nbr_lines}hydrostatic_stress", hydrostatic_stress)
#
#        if steam_pressure is not None:
#            self.setValueByName(f"{self.__nbr_lines}steam_pressure", steam_pressure)
#
#        self.__nbr_lines -= 1

