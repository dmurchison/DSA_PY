# Easy Two Pointer Problems

class ValidPalindromeSolution:
    """
    Class to check if a given string is a palindrome.
    """

    def is_palindrome(self, s: str) -> bool:
        """
        Checks if the given string is a palindrome.

        Args:
            s (str): The input string.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Convert the string to lowercase
        s = s.lower()
        # Remove all non-alphanumeric characters
        nums = "0123456789"
        for num in nums:
            s = s.replace(num, "")
        # Return True if the string is equal to its reverse
        return s == s[::-1]

print(ValidPalindromeSolution().is_palindrome("racecar"))  # True
print(ValidPalindromeSolution().is_palindrome("kaYaK"))  # True
print(ValidPalindromeSolution().is_palindrome("hello"))  # False
print()


class PrimeNumberChecker:
    def is_prime(self, num: int) -> bool:
        ans = True
        for n in range(2, num):
            if num % n == 0:
                ans = False
        return ans

print(PrimeNumberChecker().is_prime(9)) # -> False
print(PrimeNumberChecker().is_prime(5)) # -> True
print(PrimeNumberChecker().is_prime(8)) # -> False
print(PrimeNumberChecker().is_prime(3)) # -> True

