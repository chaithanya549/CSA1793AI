# Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Length
length = len(nested_list)
print("Length of nested list:", length)

# Concatenation
concatenated_list = [1, 2, 3] + [4, 5, 6]
print("Concatenated list:", concatenated_list)

# Membership
is_member = 5 in concatenated_list
print("Is 5 a member of concatenated_list:", is_member)

# Iteration
for sub_list in nested_list:
    for item in sub_list:
        print("Item:", item)

# Indexing
index = concatenated_list[2]
print("Item at index 2:", index)

# Slicing
sliced_list = concatenated_list[1:3]
print("Sliced list:", sliced_list)
