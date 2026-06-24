
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


class Printable(abc.ABC):
    def __init__(self, template):
        # Here template is a module, not the function
        self.__template = template
        self.__path     = ""
    
    
    def print(self):
        with open(f"{self.__path}input_{self.getName()}.txt", 'w') as file:
            # Here template is a module, not the function, so we have to call the .template function
            file.write(self.__template.template(self))
    
    def getPath(self) -> str:
        return self.__path

    def setPath(self, new_path: str):
        self.__path = new_path
        if len(self.__path) != 0 and self.__path[-1] != '/':
            self.__path += '/'
