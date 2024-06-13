
# O(1) Constant Time
## An algorithm whose time complexity doesn't change with input size. It is that simple!
## For example, getting the first element from a list.
## The input size doesn't affect this algorithm, because the first element is always first no matter how much input size is.

def get_first(data):
    return data[0]

data = [1, 2, 3, 4]
get_first(data)


# O(logn) Logarithmic Time
## Here is a quick reference for "What is a Logarithm": https://byjus.com/maths/logarithms/.
## A logarithmic algorithm splits a list or other data structure into smaller pieces every time it runs.
## The best example of an algorithm that has an O(logn) Time Complexity is "Binary Search".
## Binary search must be performed on a sorted list.

# Iterative Binary Search Function
# It returns the index of x in the given list if present,
# else returns -1

def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore the left half
        if lst[mid] < x:
            low = mid + 1
        # If x is smaller, ignore the right half
        elif lst[mid] > x:
            high = mid - 1
        # means x is present in mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

# Test list
lst = [2, 3, 4, 10, 40]
x = 4

# Function call
result = binary_search(lst, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")

