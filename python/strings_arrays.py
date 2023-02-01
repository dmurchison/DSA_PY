# Intersection of Two Arrays
def intersection2(list1, list2):
  s1 = set(list1)
  return s1

print('INTERSECTION')
print(intersection2([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
print(intersection2([2,4,6], [4,2])) # -> [2,4]
print(intersection2([4,2,1], [1,2,4,6])) # -> [1,2,4]
print(intersection2([0,1,2], [10,11])) # -> []
print()


# Binary Search
def binary_search(array, target):
  if len(array) == 0:
    return -1
  mid = len(array) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array[:mid], target)
  else:
    result = binary_search(array[mid+1:], target)
    if result == -1:
      return -1
    else:
      return mid + 1 + result

print(binary_search([1,2,3,4,5,6,7,8,9,10], 5)) # -> 4
print(binary_search([1,2,3,4,5,6,7,8,9,10], 10)) # -> 9
print(binary_search([1,2,3,4,5,6,7,8,9,10], 1)) # -> 0
print()


# X Or Trick

