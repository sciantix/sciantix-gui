
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
from .. import config
from .. import printable


# For this class, the options names (which serves as keys) are precede by the line index
# For Exemple :
#       0time
# Is the time value for the 1st line

class InputHistory(InputFile.InputFile, printable.Printable):
    def __init__(self, has_steam_pressure: bool = False):
        InputFile.InputFile.__init__(self, "input_history")
        printable.Printable.__init__(self, printable.history_template)

        self.__nbr_lines          = 1
        self.__has_steam_pressure = has_steam_pressure

        # Base setup : seting up the first line
        self.addOptionInterval("0time",               0,    config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval("0temperature",        1273, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval("0fission_rate",       1e19, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval("0hydrostatic_stress", 0,    config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

        if has_steam_pressure:
            self.addOptionInterval("0steam_pressure", 0, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

    
    def getNbrLines(self) -> int:
        return self.__nbr_lines

    def hasSteamPressure(self) -> bool:
        return self.__has_steam_pressure

    def toggleSteamPressure(self):
        if not self.__has_steam_pressure:
            self.__has_steam_pressure = True
            for i in range(self.__nbr_lines):
                self.addOptionInterval(f"{i}steam_pressure", 0, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

    def getLineNames(self):
        if self.__has_steam_pressure:
            line = (
                "time",
                "temperature",
                "fission_rate",
                "hydrostatic_stress",
                "steam_pressure",
            )
        else:
            line = (
                "time",
                "temperature",
                "fission_rate",
                "hydrostatic_stress",
            )

        return line
    
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

        self.addOptionInterval(f"{self.__nbr_lines}time",               time,               config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{self.__nbr_lines}temperature",        temperature,        config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{self.__nbr_lines}fission_rate",       fission_rate,       config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{self.__nbr_lines}hydrostatic_stress", hydrostatic_stress, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

        if steam_pressure is not None:
            self.addOptionInterval(f"{self.__nbr_lines}steam_pressure", steam_pressure, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

        self.__nbr_lines += 1
    
    def __moveLine(self, index, line: tuple):
        if len(line) > 5 or (len(line) == 5 and self.__has_steam_pressure):
            raise TypeError
        if not (0 <= index < self.__nbr_lines):
            raise IndexError

        if self.__has_steam_pressure:
            time, temperature, fission_rate, hydrostatic_stress, steam_pressure = line
            self.addOptionInterval(f"{index}steam_pressure", steam_pressure, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        else:
            time, temperature, fission_rate, hydrostatic_stress = line

        self.addOptionInterval(f"{index}time",               time,               config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{index}temperature",        temperature,        config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{index}fission_rate",       fission_rate,       config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{index}hydrostatic_stress", hydrostatic_stress, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

    def deleteLineByNbr(self, index: int):
        if not (0 <= index < self.__nbr_lines):
            raise IndexError
        
        self.removeOptionByName(f"{index}time")
        self.removeOptionByName(f"{index}temperature")
        self.removeOptionByName(f"{index}fission_rate")
        self.removeOptionByName(f"{index}hydrostatic_stress")

        if self.__has_steam_pressure:
            self.removeOptionByName(f"{index}steam_pressure")

        for i in range(index, self.__nbr_lines-1):
            self.__moveLine(i, self.getLineByNbr(i+1))
        
            self.removeOptionByName(f"{i+1}time")
            self.removeOptionByName(f"{i+1}temperature")
            self.removeOptionByName(f"{i+1}fission_rate")
            self.removeOptionByName(f"{i+1}hydrostatic_stress")

            if self.__has_steam_pressure:
                self.removeOptionByName(f"{i+1}steam_pressure")

        self.__nbr_lines -= 1
