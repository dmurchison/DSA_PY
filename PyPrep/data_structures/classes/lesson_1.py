# My Easy Practice Problems...

# Is Even

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
