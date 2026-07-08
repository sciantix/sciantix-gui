
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

    Version : 1.4.0
    Year :    2026
    Authors : G. Léandre
"""


import os

import classes


print("Setup...")

test_path = "test_templates/"

"""
print(f"Emptying the test directory ({test_path})...")
for elt in os.listdir(f"./{test_path}"):
    os.remove(f"./{test_path}{elt}")
"""

print("\n+----------------------------------------+")
print("|   Testing the OutputFiles sub-module   |")
print("+----------------------------------------+\n")

print("\n+----------------------------------+")
print("|   Testing the OutputFile class   |")
print("+----------------------------------+\n")

print("\tInstanciating the class...")
out = classes.OutputFile()

print(f"\tReading from {test_path}...")
out.setPath(test_path)
out.read()

print(f"\tThe nbr of line is : {out.getNbrLines()}")

print(f"\tThe first line is : {out.getLineByNbr(0)}")

print("\tAdding a line...")
out.addLine([69 for i in range(34)])
print(f"\tThe ne nbr of line is : {out.getNbrLines()}")
print(f"\tThe new line is : {out.getLineByNbr(out.getNbrLines()-1)}")

print(f"\tasking for a line that doen't exist ({out.getNbrLines()+10})...")
try:
    out.getLineByNbr(out.getNbrLines()+10)
except IndexError:
    print("\t\tIndexError...")

print("\tsetting the first row time value (6)...")
out.setValueByName("0time", 6)
print(f"\tThe new value is : {out.getValueByName('0time')}")
print(f"\tThe new line is : {out.getLineByNbr(0)}")

print("\tAsking for an option that doen't exist (6scale)...")
try:
    out.getValueByName("6scale")
except KeyError:
    print("\t\tKeyError...")


print()
