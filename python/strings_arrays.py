print('windowsTest')

a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]

# print(a)
# print(b)

def intersection2(list1, list2):
  s1 = set(list1)
  return s1

print('INTERSECTION')
print(intersection2([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
print(intersection2([2,4,6], [4,2])) # -> [2,4]
print(intersection2([4,2,1], [1,2,4,6])) # -> [1,2,4]
print(intersection2([0,1,2], [10,11])) # -> []
# a = Array (0..5000)
# b = Array (0..5000)
# print(intersection(a, b)) # -> [0,1,2,3,..., 4999]


def uncompressed(s):
   