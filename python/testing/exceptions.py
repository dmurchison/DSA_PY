sample_dict = {"a": 1, "b": 2, "c": 3}

print(sample_dict)

try:
    print("This will work", sample_dict["a"])
    # print("This will not work", sample_dict["d"])
except KeyError as e:
    print("Oh no, you tried to access a key that doesn't exist!", str(e))
finally:
    print("This will always run")

print("We made it to the end!")

a = 1
b = 0
c = None
try:
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero!")
    c = a / 1
except ZeroDivisionError as e:
    print("Oh no, you tried to divide by zero!", str(e))

# print(a / b)
print("We made it to the end!")


