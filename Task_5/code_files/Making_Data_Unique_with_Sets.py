# create a list with duplicate items
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]

# convert the list to a set to remove duplicates
unique_set = set(my_list)

# convert the set back to a list
unique_list = list(unique_set)

# print the original list and the unique list
print("Original list:", my_list)
print("Unique list:", unique_list)
