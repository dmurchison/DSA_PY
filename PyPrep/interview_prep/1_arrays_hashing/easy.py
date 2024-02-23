from typing import List


# EASY PROBLEMS
class DuplicateSolution:
    """
    Class to check if a list contains duplicate elements.
    """

    def contains_duplicate(self, nums: list) -> bool:
        """
        Checks if the given list contains duplicate elements.

        Args:
            nums (list): The list of numbers to check.

        Returns:
            bool: True if the list contains duplicate elements, False otherwise.
        """
        return len(nums) != len(set(nums))

print(DuplicateSolution().contains_duplicate([1,2,2,3,4,5,6])) # True
print(DuplicateSolution().contains_duplicate([1,2,3,4,5,6])) # False
print()


# Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram
# of s. An anagram is when the two strings can be written using the exact same
# letters (so you can just rearrange the letters to get a different phrase or
# word).

class ValidAnagramSolution:
    """
    Class to check if two strings are anagrams of each other.
    """

    def is_anagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """
        # If the length of th strings are not equal, they cannot be anagrams.
        if len(s) != len(t):
            return False
        # Now that we know the strings are the same length, we can create dicts
        # to store the counts of each character in the strings.
        s_dict = {}
        t_dict = {}
        # Iterate through the strings and add the counts to the dicts.
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        return s_dict == t_dict


print(ValidAnagramSolution().is_anagram("anagram", "nagaram")) # True
print(ValidAnagramSolution().is_anagram("rat", "car")) # False
print(ValidAnagramSolution().is_anagram("a", "ab")) # False
print(ValidAnagramSolution().is_anagram("ab", "a")) # False
print(ValidAnagramSolution().is_anagram("aacc", "ccac")) # False
print(ValidAnagramSolution().is_anagram("racecar", "racecar")) # True
print()



# Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

class Solution3:
    def right_side_list(self, nums: List[int]) -> List[int]:
        # Set -1 to a variable to be used during the iteration.
        rightMax = -1
        # Iterate backwards through the nums array.
        for i in range(len(nums) - 1, -1, -1):
            # Max of nums[i] and the current rightMax gets saved to newMax var.
            newMax = max(rightMax, nums[i])
            # Replace nums[i] with the highest value to the right.
            nums[i] = rightMax
            # Set the new rightMax to be the result of the last number and start the loop over.
            rightMax = newMax
        return nums


print(Solution3().right_side_list([1,12,3,5,-5,2])) # [12,5,5,2,2,-1]
print(Solution3().right_side_list([8,5,10,22,-14,12,5,8])) # [22,22,22,12,12,8,8,-1]

# This is the same problem as above, but with a different approach.

def replaceElements(arr: List[int]) -> List[int]:
    """
    Replaces each element in the array with the maximum element to its right.

    Args:
        arr (List[int]): The input array.

    Returns:
        List[int]: The modified array with each element replaced by the maximum element to its right.
    """
    # Set the last element to -1.
    arr[-1] = -1
    # Set the max value to the last element.
    maxVal = arr[-1]
    # Iterate backwards through the array.
    for i in range(len(arr) - 2, -1, -1):
        # Set the current element to the max value.
        arr[i] = maxVal
        # Set the max value to the max of the current element and the max value.
        maxVal = max(arr[i], maxVal)
    return arr

print(replaceElements([1,12,3,5,-5,2])) # [12,5,5,2,2,-1]
print(replaceElements([8,5,10,22,-14,12,5,8])) # [22,22,22,12,12,8,8,-1]
print()

