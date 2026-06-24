
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

    Version : 1.1.0
    Year :    2026
    Authors : G. Léandre
"""


import abc

from ..InputFields import SetInputField, IntervalInputField


class InputFile(abc.ABC):
    def __init__(self, name: str, ):
        self.__options = dict()
        self.__name    = name


    def getName(self) -> str:
        return self.__name
    
    def getOptionsNames(self) -> list[str]:
        return list(self.__options.keys())
    
    def addOptionSet(self, name: str, value: int | float, value_set: set[int|float] | list[int|float] | tuple[int|float]):
        if name in self.__options.keys():
            raise KeyError("You can't add this option : this name is already taken")
        
        self.__options[name] = SetInputField.SetInputField(value, value_set)
    
    def addOptionInterval(self, name: str, value: int | float, value_min: int | float, value_max: int | float):
        if name in self.__options.keys():
            raise KeyError("You can't add this option : this name is already taken")
        
        self.__options[name] = IntervalInputField.IntervalInputField(value, value_min, value_max)
    
    def removeOptionByName(self, name: str):
        if name not in self.__options.keys():
            raise KeyError("You can't remove this option : this name is already taken")
        
        self.__options.pop(name)

    def getValueByName(self, name: str):
        if name not in self.__options.keys():
            raise KeyError("No option with this name exist")

        return self.__options[name].getValue()

    def setValueByName(self, name: str, new_value):
        if name not in self.__options.keys():
            raise KeyError("No option with this name exist")

        self.__options[name].setValue(new_value)
