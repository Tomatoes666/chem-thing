from chem_elements import *

def total_weight(*arg):
	total = 0
	for x in range(0, len(arg)):
		total += arg[x].mw
	return total

"""for x in range(0, int(input("How many things? "))):
	mol_weight += total_weight(my_dict[input()])*int(input("how much? "))"""

mol_weight = 0

question = int(input("Convert mole to gram or vice versa 1 or 2?: "))

if question == 1:
    total_moles = float(input("Input amount of moles: "))

elif question == 2:
    total_grams = float(input("Input amount of grams: "))

x = input("Input elements, afterwards 'done': ")

while x != ("done"):
    mol_weight += total_weight(my_dict[x])*int(input("how many? "))
    x = input("Input elements, afterwards 'done': ")
if 'total_grams' in globals():
    print("total grams is ",total_grams/mol_weight, "with %d moles" % mol_weight)
elif 'total_moles' in globals():
    print(total_moles*mol_weight)

else:
    print("wtf")
