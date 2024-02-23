my_dict = {"a": 1, "b": 2, "c": 3}
my_array = [1, 2, 3, 4, 5]
my_int = 123

string_a = "Hellooo"
string_b = "ooolleH"
dict_a = {}
dict_b = {}

for i in range(len(string_a)):
    dict_a[string_a[i]] = dict_a.get(string_a[i], 0) + 1
for i in range(len(string_b)):
    dict_b[string_b[i]] = dict_b.get(string_b[i], 0) + 1


print(dict_a == dict_b)
