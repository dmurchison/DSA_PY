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
