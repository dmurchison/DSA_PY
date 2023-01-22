# Tidying messy data

country = '107, Golf, United States, Gold, 7'
parts = country.split (',')
new = int (parts [0]) + 1
print(new)
print()

# None
this_var_is_none = None
print(this_var_is_none, type(this_var_is_none))
print()


# Formatting Strings
name = 'John'
age = 36.12333
zip_code = 1234
output = f"{name} is {age:.2f} years old, and his zip code is {zip_code:05d}."  # f-string
# TODO: This is a cool comment.
print(output)
print()

# If Else Statements
random_list = [1, 'a', 0, False, True, '0']
for el in random_list:
    print(el)

def add_subtract_numbers(num1, num2 = 2):
    return num1 + num2, num1 - num2


*_, last = add_subtract_numbers(1)  # (3, -1)
print(last)  # -1



