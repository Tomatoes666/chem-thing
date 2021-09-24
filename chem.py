from chem_elements import *

def total_weight(*arg):
	total = 0
	for x in range(0, len(arg)):
		total += arg[x].mw
	return total

"""for x in range(0, int(input("How many things? "))):
	mol_weight += total_weight(my_dict[input()])*int(input("how much? "))"""

mol_weight = 0



x = input("Input elements, afterwards 'done': ")
while x != ("done"):
	mol_weight += total_weight(my_dict[x])*int(input("how many? "))
	x = input("Input elements, afterwards 'done': ")

print(mol_weight)
