
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

Version: 1.0.0
Year: 2026
Authors: G. Léandre
"""

import abc


class InputFIle(abc.ABC):
    def __init__(self, name: str):
        __options = dict()
        __name    = name

    def getName(self) -> str:
        return __name
    
    def getOptionsNames(self) -> list[str]:
        return list(__options.keys())

    def getValueByName(self, name: str):
        if name not in __options.keys():
            raise KeyError

        return __options[name]

    def setValueByName(self, new_value):
        pass        # TODO
