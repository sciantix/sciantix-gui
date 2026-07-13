
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


from . import InputField


class IntervalInputField(InputField.InputField):
    def __init__(self, value: int | float, value_min: int | float, value_max: int | float):
        super().__init__(value)

        if (value_min > value_max):
            raise ValueError("You can't have an empty interval : value_min <= value_max has to be respected")
        
        self.__value_min = value_min
        self.__value_max = value_max
        
        if not self.__checkValue(value):
            raise ValueError(f"You can't use this value, It is not in the interval [{self.__value_min}, {self.__value_max}]")
    
    
    def __checkValue(self, new_value: int | float) -> bool:
        return self.__value_min <= new_value <= self.__value_max
    
    def clampValue(self, new_value: int | float) -> int | float:
        if new_value < self.__value_min:
            ans = self.__value_min
        elif new_value > self.__value_max:
            ans = self.__value_max
        else:
            ans = new_value

        return ans

    # We have to re-implement it for it to use the IntervalInputField __checkValue and not the InputField one
    def setValue(self, new_value: int | float):
        if not self.__checkValue(new_value):
            raise ValueError(f"You can't use this value, It is not in the interval [{self.__value_min}, {self.__value_max}]")

        super().setValue(new_value)
