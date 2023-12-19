from cmath import sqrt
from math import floor


def greet(s):
  return 'hey ' + s
  
print(greet("Duncan")) # -> "hey Duncan"

def max_value(nums):
  max = float('-inf')
  for num in nums:
    if num > max:
      max = num
  return max

print(max_value([4,7,2,8,10,9])) # -> 10``


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
