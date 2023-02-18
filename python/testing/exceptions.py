sample_dict = {"a": 1, "b": 2, "c": 3}

print(sample_dict)

try:
    print("This will work", sample_dict["a"])
    print("This will not work", sample_dict["d"])
except KeyError as e:
    print("Oh no, you tried to access a key that doesn't exist!", str(e))
except Exception as e:
    print("Oh no, don't be an idiot!", str(e))


a = 1
b = 0
try:
    if b == 0:
        raise ZeroDivisionError("You can't divide by zero!")
    c = a / b
except KeyError as e:
    print("Oh no, you tried to access a key that doesn't exist!", str(e))


print("We made it to the end!")

