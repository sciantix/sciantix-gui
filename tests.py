
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

    Version : 1.0.0
    Year :    2026
    Authors : G. Léandre
"""


import classes


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


print("\n\n+---------------------------------------+")
print("|   Testing the InputFiles sub-module   |")
print("+---------------------------------------+\n")

print("\n+------------------------------------+")
print("|   Testing the InputHistory class   |")
print("+------------------------------------+\n")

print("\tInstanciating the class...")
A_hist  = classes.InputHistory()

print(f"\tThe nbr of line is : {A_hist.getNbrLines()}")

print(f"\tThe first line is : {A_hist.getLineByNbr(0)}")

print("Adding a line...")
A_hist.addLine(5500, 1273, 1e19, 0)
print(f"\tThe ne nbr of line is : {A_hist.getNbrLines()}")
print(f"\tThe new line is : {A_hist.getLineByNbr(1)}")

print("\tasking for a line that doen't exist (6)...")
try:
    A_hist.getLineByNbr(6)
except IndexError:
    print("\t\tIndexError...")


A_init  = classes.InputInitialCondition()
A_scale = classes.InputScalingFactor()
A_set   = classes.InputSettings()


print()
