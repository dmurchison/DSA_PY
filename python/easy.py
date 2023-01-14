from cmath import sqrt
from math import floor


# MAX VALUE
# Write a function max_value(nums) that takes in a list of numbers and returns 
# the largest number in the list.

def max_value(nums):
  max = float('-inf')
  for num in nums:
    if num > max:
      max = num

  return max

print(max_value([4,7,2,8,10,9])) # -> 10
print(max_value([1,2,3,4,5,6,7,8,9,10])) # -> 10
print(max_value([10,9,8,7,6,5,4,3,2,1])) # -> 10
print(max_value([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # -> 20
print(max_value([20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])) # -> 20
print(max_value([1,2,3,4,5,6,7,8,9,10,11,12,13,17,18,19,20,21])) # -> 21
print(max_value([21,20,19,18,17,16,15,14,1,7,6,5,4,3,2,1])) # -> 21
print()


# PRIME
# Write a function is_prime(n) that takes in a number and returns a boolean 
# indicating whether it is prime. A prime number is only divisible by 1 and 
# itself.

def is_prime(n):
  if n < 2:
    return False

  for i in range(2, n):
    if n % i == 0:
      return False

  return True 

print(is_prime(2)) # -> True
print(is_prime(3)) # -> True
print(is_prime(4)) # -> False
print(is_prime(5)) # -> True
print(is_prime(6)) # -> False
print(is_prime(7)) # -> True
print(is_prime(8)) # -> False
print(is_prime(25)) # -> False
print(is_prime(31)) # -> True
print(is_prime(2017)) # -> True
print(is_prime(2048)) # -> False
print(is_prime(1)) # -> False
print(is_prime(713)) # -> False
print()


# PRIME FACTORS
# Write a function prime_factors(n) that takes in a number and returns an array 
# containing all the prime factors of the given number.

def prime_factors(n):
  factors = []
  for i in range(2, n):
    if n % i == 0 and is_prime(i):
      factors.append(i)

  return factors

print(prime_factors(12)) # -> [2,3]
print(prime_factors(24)) # -> [2,3]
print(prime_factors(25)) # -> [5]
print(prime_factors(60)) # -> [2,3,5]
print(prime_factors(7)) # -> []
print(prime_factors(11)) # -> []
print(prime_factors(2017)) # -> []
print(prime_factors(2018)) # -> [2, 1009]
print()



# FIBONACCI
# Write a function fibonacci(n) that takes in a number length and returns the
# fibonacci sequence up to the given length.

def fibonacci(n):
  if n == 0:
    return []
  if n == 1:
    return [0]
  if n == 2:
    return [0, 1]

  fibs = [0, 1]
  while len(fibs) < n:
    fibs.append(fibs[-1] + fibs[-2])

  return fibs

print(fibonacci(0)) # -> []
print(fibonacci(1)) # -> [0]
print(fibonacci(2)) # -> [0, 1]
print(fibonacci(3)) # -> [0, 1, 1]
print(fibonacci(4)) # -> [0, 1, 1, 2]
print(fibonacci(5)) # -> [0, 1, 1, 2, 3]
print(fibonacci(6)) # -> [0, 1, 1, 2, 3, 5]
print(fibonacci(7)) # -> [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(8)) # -> [0, 1, 1, 2, 3, 5, 8, 13]
print()



# BINARY SEARCH
# Write a function binary_search(array, target) that takes in a sorted array of
# numbers and a target number as arguments. The function should return the
# index of the target in the array if it is present. If it is not present, the
# function should return -1.

def binary_search(array, target):
  left = 0
  right = len(array) - 1

  while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 1)) # -> 0
print(binary_search([1,2,3,4,5,6,7,8,9,10], 2)) # -> 1
print(binary_search([1,2,3,4,5,6,7,8,9,10], 3)) # -> 2
print(binary_search([1,2,3,4,5,6,7,8,9,10], 4)) # -> 3
print(binary_search([1,2,3,4,5,6,7,8,9,10], 5)) # -> 4
print(binary_search([1,2,3,4,5,6,7,8,9,10], 6)) # -> 5
print(binary_search([1,2,3,4,5,6,7,8,9,10], 7)) # -> 6
print(binary_search([1,2,3,4,5,6,7,8,9,10], 8)) # -> 7
print(binary_search([1,2,3,4,5,6,7,8,9,10], 9)) # -> 8
print(binary_search([1,2,3,4,5,6,7,8,9,10], 10)) # -> 9
print(binary_search([1,2,3,4,5,6,7,8,9,10], 11)) # -> -1
print(binary_search([1,2,3,4,5,6,7,8,9,10], 0)) # -> -1
print()



