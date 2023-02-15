
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



def my_function(s):
    my_hash = {}
    for i in s:
        my_hash[i] = 1 + my_hash.get(i, 0)
    return my_hash.get("a")
    

my_string = "abcdefghijklmnopqrrstuvvauxyz"
print(my_function(my_string))
