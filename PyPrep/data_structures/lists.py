# LIST
# A list is a collection which is ordered and changeable.
# Allows duplicate members.
list = ["apple", "banana", "cherry"]
print(list[1]) # banana
print(list[-1]) # cherry
print(list[2:]) # ["cherry"]
print(list[:2]) # ["apple", "banana"]
print(list[1:2]) # ["banana"]
print(list[1:-1]) # ["banana"]
print()
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
print()
returned_value = example_list.pop()
print("Pop Example # Array.pop()")
print("Array.pop() - ",returned_value)
print("Array - ", example_list)
print()

