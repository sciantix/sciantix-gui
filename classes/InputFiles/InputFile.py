
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


import abc


class InputFile(abc.ABC):
    def __init__(self, name: str, ):
        self.__options = dict()
        self.__name    = name


    def getName(self) -> str:
        return self.__name
    
    def getOptionsNames(self) -> list[str]:
        return list(self.__options.keys())

    def getValueByName(self, name: str):
        if name not in self.__options.keys():
            raise KeyError

        return self.__options[name].getValue()

    def setValueByName(self, name: str, new_value):
        if name not in self.__options.keys():
            # To add a new option, also used to setup the base options
            self.__options[name] = setValue(new_value)
        else:
            self.__options[name].setValue(new_value)
