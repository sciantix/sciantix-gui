
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

    Version : 1.4.1
    Year :    2026
    Authors : G. Léandre
"""


import abc


class MultiLines(abc.ABC):
    def __init__(self):
        self.__nbr_lines = 0

    
    def getNbrLines(self) -> int:
        return self.__nbr_lines
    
    def _incrementLineNbr(self):
        self.__nbr_lines += 1
    
    def _decrementLineNbr(self):
        self.__nbr_lines -= 1
    
    def getLineByNbr(self, index: int) -> tuple:
        # Has to be re-implemented
        return tuple()
    
    def addLine(self, time: int, *args, **kwargs):
        # Has to be re-implemented
        self._incrementLineNbr()
    
    def deleteLineByNbr(self, index: int):
        # Has to be re-implemented
        self._decrementLineNbr()
