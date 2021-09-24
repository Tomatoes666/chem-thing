from chem_elements import *
from chem_functions import total_weight

mol_weight = 0

question = int(input("Convert mole to gram or vice versa 1 or 2?: "))
if question == 1:
    total_moles = float(input("Input amount of moles: "))
elif question == 2:
    total_grams = float(input("Input amount of grams: "))


ele = input("Input elements, afterwards 'done': ")

while ele != ("done"):
    mol_weight += total_weight(my_dict[ele])*int(input("how many? "))
    ele = input("Input elements, afterwards 'done': ")
if 'total_grams' in globals():
    print("total grams is ",total_grams/mol_weight, "with %d moles" % mol_weight)
elif 'total_moles' in globals():
    print(total_moles*mol_weight)

else:
    print("wtf")
