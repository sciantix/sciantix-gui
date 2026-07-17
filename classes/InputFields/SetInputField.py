
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

    Version : 1.4.5
    Year :    2026
    Authors : G. Léandre
"""


from . import InputField


class SetInputField(InputField.InputField):
    __slots__ = [
        # From the InputField super-class
        "__value",
        
        # From the SetInputField class
        "__value_set"
    ]

    def __init__(self, value: int | float, value_set: set[int|float] | list[int|float] | tuple[int|float]):
        super().__init__(value)
        
        self.__value_set = set(value_set)

        if not self.__checkValue(value):
            raise ValueError(f"You can't use this value, It does exist in the set : {self.__value_set}")


    def __checkValue(self, new_value: int | float) -> bool:
        return new_value in self.__value_set
    
    def clampValue(self, new_value: int | float) -> int | float:
        """
        Find the nearest value in the set from new_value and return this one 
        """
        min_distance = float("inf")
        ans = new_value

        if not self.__checkValue(new_value):
            for elt in self.__value_set:
                if abs(elt - new_value) < min_distance:
                    min_distance = abs()
                    ans = elt

        return ans

    # We have to re-implement it for it to use the SetInputField __checkValue and not the InputField one
    def setValue(self, new_value: int | float):
        if not self.__checkValue(new_value):
            raise ValueError(f"You can't use this value, It does exist in the set : {self.__value_set}")

        super().setValue(new_value)
    
    def getSet(self) -> set[int|float]:
        return self.__value_set
