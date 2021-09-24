from chem_elements import *
from chem_functions import total_weight

mol_weight = 0

x = input("Input elements, afterwards 'done': ")
while x != ("done"):
	mol_weight += total_weight(my_dict[x])*int(input("how many? "))
	x = input("Input elements, afterwards 'done': ")

print(mol_weight)
