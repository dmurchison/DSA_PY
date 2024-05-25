
f = open('file_structure/test_file.txt', 'w')
f.write('This is going to be the first line.\n')
f.write('This is going to be the second line.\n')
f.close()


f = open('file_structure/test_file.txt', 'a')
f.write('This is going to be the third line, appended.\n')
f.write('This is the final line, appended.\n')
f.close()


# Possible to open a file in read mode
f = open('file_structure/test_file.txt', 'r')
for line in f.readlines():
    print(line)
f.close()

# Preferred way to open a file
with open('file_structure/test_file.txt', 'r') as f:  # f = open(..)
    for line in f.readlines():
        print(line)


