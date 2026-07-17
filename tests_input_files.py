
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


import os

import classes


print("Setup...")

test_path = "test_templates/input/"


print(f"Emptying the test directory ({test_path})...")
for elt in os.listdir(f"./{test_path}"):
    os.remove(f"./{test_path}{elt}")


print("\n+---------------------------------------+")
print("|   Testing the InputFiles sub-module   |")
print("+---------------------------------------+\n")

print("\n+------------------------------------+")
print("|   Testing the InputHistory class   |")
print("+------------------------------------+\n")

print("\tInstanciating the class...")
A_hist = classes.InputHistory()

print(f"\tThe nbr of line is : {A_hist.getNbrLines()}")

print(f"\tThe first line is : {A_hist.getLineByNbr(0)}")

print("\tAdding a line...")
A_hist.addLine(5500, 1273, 1e19, 0)
print(f"\tThe ne nbr of line is : {A_hist.getNbrLines()}")
print(f"\tThe new line is : {A_hist.getLineByNbr(1)}")

print("\tasking for a line that doen't exist (6)...")
try:
    A_hist.getLineByNbr(6)
except IndexError:
    print("\t\tIndexError...")

print("\tsetting the first row time value (6)...")
A_hist.setValueByName("0time", 6)
print(f"\tThe new value is : {A_hist.getValueByName('0time')}")
print(f"\tThe new line is : {A_hist.getLineByNbr(0)}")

print("\tAsking for an option that doen't exist (6scale)...")
try:
    A_hist.getValueByName("6scale")
except KeyError:
    print("\t\tKeyError...")

print(f"\tPrinting to {test_path}...")
A_hist.setPath(test_path)
A_hist.print()

print("\n+---------------------------------------------+")
print("|   Testing the InputInitialCondition class   |")
print("+---------------------------------------------+\n")

print("\tInstanciating the class...")
A_init  = classes.InputInitialCondition()

print(f"\tAccessing the layout : {A_init.getLayout()}")

print(f"\tAccessing grain_radius's value : {A_init.getValueByName('grain_radius')}")

print("\tsetting grain_radius's value (6)...")
A_init.setValueByName("grain_radius", 6)
print(f"\tThe new value is : {A_init.getValueByName('grain_radius')}")

print("\tAsking for an option that doen't exist (scale)...")
try:
    A_init.getValueByName("scale")
except KeyError:
    print("\t\tKeyError...")

print(f"\tPrinting to {test_path}...")
A_init.setPath(test_path)
A_init.print()

print("\n+------------------------------------------+")
print("|   Testing the InputScalingFactor class   |")
print("+------------------------------------------+\n")

print("\tInstanciating the class...")
A_scale = classes.InputScalingFactor()

print(f"\tAccessing resolution_rate's value : {A_scale.getValueByName('resolution_rate')}")

print("\tsetting resolution_rate's value (6)...")
A_scale.setValueByName("resolution_rate", 6)
print(f"\tThe new value is : {A_scale.getValueByName('resolution_rate')}")

print("\tAsking for an option that doen't exist (scale)...")
try:
    A_scale.getValueByName("scale")
except KeyError:
    print("\t\tKeyError...")

print(f"\tPrinting to {test_path}...")
A_scale.setPath(test_path)
A_scale.print()

print("\n+-------------------------------------+")
print("|   Testing the InputSettings class   |")
print("+-------------------------------------+\n")

print("\tInstanciating the class...")
A_set = classes.InputSettings()

print(f"\tAccessing GrainGrowth's value : {A_set.getValueByName('GrainGrowth')}")

print("\tsetting GrainGrowth's value (2)...")
A_set.setValueByName("GrainGrowth", 2)
print(f"\tThe new value is : {A_set.getValueByName('GrainGrowth')}")

print("\tAsking for an option that doen't exist (scale)...")
try:
    A_set.getValueByName("scale")
except KeyError:
    print("\t\tKeyError...")

print(f"\tPrinting to {test_path}...")
A_set.setPath(test_path)
A_set.print()


print()
