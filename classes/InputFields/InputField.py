
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

    Version : 1.3.0
    Year :    2026
    Authors : G. Léandre
"""


import abc


class InputField(abc.ABC):
    def __init__(self, value: int | float):
        self.__value = value


    # @abc.abstractmethod
    def __checkValue(self, new_value: int | float) -> bool:
        return True
    
    def getValue(self) -> int | float:
        return self.__value

    def setValue(self, new_value: int | float):
        if not self.__checkValue(new_value):
            raise ValueError("If you see this, you messed up badly...")

        self.__value = new_value
