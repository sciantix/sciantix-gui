
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


class InputHistory(InputFile):
    def __init__(self, nbr_lines: int, has_steam_pressure: bool = False):
        super().__init__("input_history")

        self.__nbr_lines          = nbr_lines
        self.__has_steam_pressure = has_steam_pressure

    
    def getNbrLines(self) -> int:
        return self.__nbr_lines
    
    def getLineByNbr(self, index: int):
        if not (0 <= index < self.__nbr_lines):
            raise IndexError

        pass        # TODO
    
    def addLine(self):
        self.__nbr_lines += 1

        # TODO
    
    def deleteLine(self, index: int):
        if not (0 <= index < self.__nbr_lines):
            raise IndexError

        self.__nbr_lines -= 1

        # TODO

