
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

    Version : 1.4.2
    Year :    2026
    Authors : G. Léandre
"""


from . import InputFile
from . import MultiLines
from .. import config
from .. import FileAccess


# For this class, the options names (which serves as keys) are precede by the line index
# For Exemple :
#       0time
# Is the time value for the 1st line

class InputHistory(InputFile.InputFile, MultiLines.MultiLines, FileAccess.Printable):
    def __init__(self, has_steam_pressure: bool = False):
        InputFile.InputFile.__init__(self, "input_history")
        MultiLines.MultiLines.__init__(self)
        FileAccess.Printable.__init__(self, FileAccess.history_template)

        self.__has_steam_pressure = has_steam_pressure

        self.__units = config.HISTORY_UNITS

        # Base setup : seting up the first lines from the basic exemple run
        if has_steam_pressure:
            self.addLine(0,    1373, 1e19, 0, 0)
            self.addLine(5500, 1373, 1e19, 0, 0)
        else:
            self.addLine(0,    1373, 1e19, 0)
            self.addLine(5500, 1373, 1e19, 0)

    
    def hasSteamPressure(self) -> bool:
        return self.__has_steam_pressure

    def toggleSteamPressure(self):
        if not self.__has_steam_pressure:
            self.__has_steam_pressure = True
            for i in range(self.getNbrLines()):
                self.addOptionInterval(f"{i}steam_pressure", 0, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        else:
            self.__has_steam_pressure = False
            for i in range(self.getNbrLines()):
                self.removeOptionByName(f"{i}steam_pressure")
    
    def getUnits(self) -> list[str]:
        return self.__units

    def getLineNames(self) -> tuple:
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
        if not (0 <= index < self.getNbrLines()):
            raise IndexError("You can't get a line that doesn't exist, index must be between 0 and InputHistory.getNbrLines()")
        
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
            raise TypeError("You need to specify the steam_pressure value if you have set it togled")

        self.addOptionInterval(f"{self.getNbrLines()}time",               time,               config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{self.getNbrLines()}temperature",        temperature,        config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{self.getNbrLines()}fission_rate",       fission_rate,       config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)
        self.addOptionInterval(f"{self.getNbrLines()}hydrostatic_stress", hydrostatic_stress, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

        if steam_pressure is not None:
            self.addOptionInterval(f"{self.getNbrLines()}steam_pressure", steam_pressure, config.HISTORY_LOWER_BOUND, config.HISTORY_UPER_BOUND)

        self._incrementLineNbr()
    
    def __moveLine(self, index, line: tuple):
        if len(line) > 5 or (len(line) == 5 and self.__has_steam_pressure):
            raise TypeError("A line should be 4; 5 if steam_pressure i togled")
        if not (0 <= index < self.getNbrLines()):
            raise IndexError("You can't move a line that doesn't exist, index must be between 0 and InputHistory.getNbrLines()")

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
        if not (0 <= index < self.getNbrLines()):
            raise IndexError("You can't delete a line that doesn't exist, index must be between 0 and InputHistory.getNbrLines()")
        
        self.removeOptionByName(f"{index}time")
        self.removeOptionByName(f"{index}temperature")
        self.removeOptionByName(f"{index}fission_rate")
        self.removeOptionByName(f"{index}hydrostatic_stress")

        if self.__has_steam_pressure:
            self.removeOptionByName(f"{index}steam_pressure")

        for i in range(index, self.getNbrLines()-1):
            self.__moveLine(i, self.getLineByNbr(i+1))
        
            self.removeOptionByName(f"{i+1}time")
            self.removeOptionByName(f"{i+1}temperature")
            self.removeOptionByName(f"{i+1}fission_rate")
            self.removeOptionByName(f"{i+1}hydrostatic_stress")

            if self.__has_steam_pressure:
                self.removeOptionByName(f"{i+1}steam_pressure")

        self._decrementLineNbr()
