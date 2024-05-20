# My Easy Practice Problems...

# Is Even

from operator import is_
from xmlrpc.client import Boolean


def is_even(num):
    """
    This function checks if a given number is even.

    Args:
        number: The number to be checked for evenness.

    Returns:
        True if the number is even, False otherwise.
    """
    return num  % 2 == 0

print(is_even(2))
print(is_even(1))
print(is_even(7))
print(is_even(10))

def gcd(a, b):
    """
    This function calculates the greatest common divisor (GCD) of two positive integers.

    Args:
        a: The first positive integer.
        b: The second positive integer.

    Returns
        The greatest common divisor of a and b
    """
    if a <= 0 or b <= 0:
        return None
    while b != 0:
        rem = a % b
        a = b
        b = rem
    return (a,b)

print(gcd(15,5))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(1,num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(8))
