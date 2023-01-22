
f = open('file_structure/test_file.txt', 'w')
f.write('This is going to be the first line.\n')
f.write('This is going to be the second line.\n')
f.close()


f = open('file_structure/test_file.txt', 'a')
f.write('This is going to be the third line, appended.\n')
f.write('This is the final line, appended.\n')
f.close()

f = open('file_structure/test_file.txt', 'r')
file_line = f.readline()
print(file_line)
file_line = f.readline()
print(file_line)
f.close()


