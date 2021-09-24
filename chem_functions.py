from chem_elements import *

#Molecular Mass, takes in any number of arguments
def total_weight(*arg):
	total = 0
	for x in range(0, len(arg)):
		total += arg[x].mw
	return total

