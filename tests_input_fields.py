
"""
-------------------------------------------------------------------------------------------------------------------------------------
     _______.  ______  __       ___      .__   __. .___________.|| __           __  __  __________      ___     ._______ ._____
    /       | /      ||  |     /   \     |  \ |  | |           |//\  \         /  /|  ||______    |    /   \    |   _   \|  _  \
   |   (----`|  ,----'|  |    /  ^  \    |   \|  | `---|  |----`   \  \   _   /  / |  |     _/  _/    /  ^  \   |  |_)  || | \  \
    \   \    |  |     |  |   /  /_\  \   |  . `  |     |  |         \  \ / \ /  /  |  |   _/  _/     /  /_\  \  |   ____/| |  )  |
.----)   |   |  `----.|  |  /  _____  \  |  |\   |     |  |          \  v   v  /   |  | _/  _/____  /  _____  \ |  |\  \ | |_/  /
|_______/     \______||__| /__/     \__\ |__| \__|     |__|           \__/^\__/    |__||__________|/__/     \__\|__| \__\|_____/

-------------------------------------------------------------------------------------------------------------------------------------

    Originally developed by G. Léandre

    Version : 1.3.0
    Year :    2026
    Authors : G. Léandre
"""


import os

import classes


# No setup needed here
"""
print("Setup...")

test_path = "test_templates/"


print(f"Emptying the test directory ({test_path})...")
for elt in os.listdir(f"./{test_path}"):
    os.remove(f"./{test_path}{elt}")
"""

print("\n+----------------------------------------+")
print("|   Testing the InputFields sub-module   |")
print("+----------------------------------------+\n")

print("\n+-------------------------------------+")
print("|   Testing the SetInputField class   |")
print("+-------------------------------------+\n")

print("\tInstanciating the class...")
B_set = classes.SetInputField(0, [0, 2])

print(f"\tThe class has the value : {B_set.getValue()}")

print("\tSetting the value to an allowed value (2)...")
B_set.setValue(2)
print(f"\tThe class has the value : {B_set.getValue()}")

print("\tSetting the value to an unallowed value (1)...")
try:
    B_set.setValue(1)
except ValueError:
    print("\t\tValueError...")
print(f"\tThe class has the value : {B_set.getValue()}")


print("\n+------------------------------------------+")
print("|   Testing the IntervalInputField class   |")
print("+------------------------------------------+\n")

print("\tInstanciating the class...")
B_int = classes.IntervalInputField(0, 0, 5)

print(f"\tThe class has the value : {B_int.getValue()}")

print("\tSetting the value to an allowed value (2)...")
B_int.setValue(2)
print(f"\tThe class has the value : {B_int.getValue()}")

print("\tSetting the value to an unallowed value (6)...")
try:
    B_int.setValue(6)
except ValueError:
    print("\t\tValueError...")
print(f"\tThe class has the value : {B_int.getValue()}")


print()
