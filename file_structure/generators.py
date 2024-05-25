import os

def populate_file(filename):
    values_to_write = ["Hello", "World", "This", "Is", "A", "Test"]
    with open(filename, "w") as out:
        for value in values_to_write:
            out.write(value)
            out.write("\n")


def read_file(filename):
    # data = []  # This is an outdated way of doing this. Use a generator instead.
    with open(filename, "r") as in_file:
        for line in in_file:
            yield line  # This is the generator version of this function.
            # data.append(line)
    # return data


def read_if_exists(filename):
    if os.path.exists(filename):
        yield from read_file(filename)
    else:
        return []

filename = "file_structure/test.txt"
populate_file(filename)
print()


# This is a shorthand generator version of the read_file function.
file_contents = (row for row in open(filename, "r"))
print(file_contents)
print()
# The forloop way of doing this is:
for line in file_contents:
    print(line)


# This is the generator version of the read_if_exists function.
file_contentz = read_if_exists(filename)
print(file_contentz)

# The next() function is used to get the next value from a generator.
line = next(file_contentz)
print(line)
another_line = next(file_contentz)
print(another_line)
anotha_one = next(file_contentz)
print(anotha_one)
# ... and so on.






