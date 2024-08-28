food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. 
food_list = food.split(',')
equipment_list = equipment.split(',')
pets_list = pets.split(',')
sleep_aids_list = sleep_aids.split(',')
# Alphabetize the contents of each cabinet.
food_list.sort()
equipment_list.sort()
pets_list.sort()
sleep_aids_list.sort()
# # print
# print("Food:", food_list)
# print("Equipment:", equipment_list)
# print("Pets:", pets_list)
# print("Sleep Aids:", sleep_aids_list)

# b) Initialize a cargo_hold list 
cargo_hold = []
# and add the cabinet lists to it.
#  cargo_hold.append(food_list)
cargo_hold.append(food_list)
cargo_hold.append(equipment_list)
cargo_hold.append(pets_list)
cargo_hold.append(sleep_aids_list)
# Print cargo_hold to verify its structure.
print(cargo_hold)



# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.



# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
