my_dict = {"a": 1, "b": 2, "c": 3}
my_array = [1, 2, 3, 4, 5]
my_int = 123

string_a = "Hellooo"
string_b = "ooolleH"
dict_a = {}
dict_b = {}

# Create a hash from a string
for i in range(len(string_a)):
    dict_a[string_a[i]] = dict_a.get(string_a[i], 0) + 1
for i in range(len(string_b)):
    dict_b[string_b[i]] = dict_b.get(string_b[i], 0) + 1

print(dict_a == dict_b)


# Create a hash from an array
hash_array = {}
for i in range(len(my_array)):
    hash_array[my_array[i]] = hash_array.get(my_array[i], 0) + 1

# Create a hash from a dictionary
hash_dict = {}
for key in my_dict:
    hash_dict[key] = my_dict[key]

# Create a hash from an integer
hash_int = hash(my_int)
print(hash_int)
print()

# Nested loops
for i in range(5):
    for j in range(5):
        print(i, j)


s = "racecar bros"
n = s.upper()
print("!".join(n, ))


st = "the jeep rolled down the hill"
for i in range(len(st)):
    print(st[i], st[i+1])
