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


# TUPLE
# A tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members.
tuple = ("apple", "banana", "cherry")
print(tuple[1]) # banana
print(tuple[-1]) # cherry
print(tuple[2:]) # ("cherry")
print(tuple[:2]) # ("apple", "banana")
print(tuple[1:2]) # ("banana")
print(tuple[1:-1]) # ("banana")
print()


# SET
# A set is a collection which is unordered and unindexed. No duplicate members.
set = {"apple", "banana", "cherry"}
print(set) # {"apple", "banana", "cherry"}
set.add("orange")
print(set) # {"apple", "banana", "cherry", "orange"}
set.remove("banana")
print(set) # {"apple", "cherry", "orange"}
set.discard("banana")
print(set) # {"apple", "cherry", "orange"}
set.pop()
print(set) # {"cherry", "orange"}
set.clear()
print(set) # set()
print()


# DICTIONARY
# A dictionary is a collection which is unordered, changeable and indexed. 
# No duplicate members.
hash = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(hash) # {"brand": "Ford", "model": "Mustang", "year": 1964}
print(hash["model"]) # Mustang
print(hash.get("model")) # Mustang
hash["year"] = 2018
print(hash) # {"brand": "Ford", "model": "Mustang", "year": 2018}
for x in hash:
    print(x) # brand model year
for x in hash:
    print(hash[x]) # Ford Mustang 2018
for x in hash.values():
    print(x) # Ford Mustang 2018
for x, y in hash.items():
    print(x, y) # brand Ford model Mustang year 2018
if "model" in hash:
    print("Yes, 'model' is one of the keys in the hash dictionary") # Yes, 'model' is one of the keys in the hash dictionary
print(len(hash)) # 3
hash["color"] = "red"
print(hash) # {"brand": "Ford", "model": "Mustang", "year": 2018, "color": "red"}
hash.pop("model")
print(hash) # {"brand": "Ford", "year": 2018, "color": "red"}
hash.popitem()
print(hash) # {"brand": "Ford", "year": 2018}
hash.clear()
print(hash) # {}
print()


# LIST COMPREHENSION
# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.
#
# Syntax:
# new_list = [expression for item in iterable if condition == True]
#
# Example:
new_list = [x for x in range(10)]
print(new_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [x for x in range(10) if x < 5]
print(new_list) # [0, 1, 2, 3, 4]

fruits = ["apple", "banana", "cherry"]

new_list = [x.upper() for x in fruits]
print(new_list) # ["APPLE", "BANANA", "CHERRY"]

new_list = [x for x in fruits if "a" in x]
print(new_list) # ["apple", "banana"]

new_list = [x if x != "banana" else "orange" for x in fruits]
print(new_list) # ["apple", "orange", "cherry"]
print()



# DICTIONARY COMPREHENSION
# Dictionary comprehension offers a shorter syntax when you want to create a new dictionary
# based on the keys and values of an existing dictionary.
#
# Syntax:
# new_dict = {new_key:new_value for item in iterable}
#
# Example:
fruits = ["apple", "banana", "cherry"]

new_dict = {x: x.upper() for x in fruits}
print(new_dict) # {"apple": "APPLE", "banana": "BANANA", "cherry": "CHERRY"}

new_dict = {x: len(x) for x in fruits}
print(new_dict) # {"apple": 5, "banana": 6, "cherry": 6}

new_dict = {x: x for x in fruits if x != "banana"}
print(new_dict) # {"apple": "apple", "cherry": "cherry"}

new_dict = {x: x if x != "banana" else "orange" for x in fruits}
print(new_dict) # {"apple": "apple", "banana": "orange", "cherry": "cherry"}

new_dict = {x: x for x in fruits}
print(new_dict) # {"apple": "apple", "banana": "banana", "cherry": "cherry"}

new_dict = {x: x for x in fruits if x != "banana"}
print(new_dict) # {"apple": "apple", "cherry": "cherry"}

new_dict = {x: x if x != "banana" else "orange" for x in fruits}
print(new_dict) # {"apple": "apple", "banana": "orange", "cherry": "cherry"}

new_dict = {x: x for x in fruits}
print(new_dict) # {"apple": "apple", "banana": "banana", "cherry": "cherry"}






