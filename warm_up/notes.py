# Tidying messy data

country = '107, Golf, United States, Gold, 7'
parts = country.split (',')
new = int (parts [0]) + 1
print(new)
print()
# Variables and types

# None
this_var_is_none = None
print(this_var_is_none, type(this_var_is_none))


example_list = [1, 2, 3, 4, 5]
example_list_2 = example_list[2:4]
print(example_list_2)
print()
example_list += example_list_2
print("Addition Example # Array += Array_2")
print(example_list)
print()
example_list.append(example_list_2)
print("Append Example # Array.append(Array)")
print(example_list)
print()
example_list = example_list[2:]
print("Slicing Example # Array[2:]")
print(example_list)


