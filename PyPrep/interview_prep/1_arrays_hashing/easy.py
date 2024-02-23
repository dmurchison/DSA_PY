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
print(DuplicateSolution().contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
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
print(ValidAnagramSolution().is_anagram("racecar", "racecar")) # True
print()



# Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

class ReplaceElementsSolution:
    """
    Class to replace each element in an array with the maximum element to its right.
    """

    def right_side_list(self, arr: List[int]) -> List[int]:
        """
        Replaces each element in the array with the maximum element to its right.

        Args:
            arr (List[int]): The input array.

        Returns:
            List[int]: The modified array with each element replaced by the maximum element to its right.
        """
        # Create a new list to store the results.
        result = []
        right_el = -1
        # Iterate backwards through the array.
        for i in range(len(arr) -1, -1, -1):
            # Set the current element to the max of the current element and the right element.
            result.append(right_el)
            right_el = max(right_el, arr[i])
        # Reverse the list and return it.
        return result[::-1]


print(ReplaceElementsSolution().right_side_list([1,12,3,5,-5,2])) # [12,5,5,2,2,-1]
print(ReplaceElementsSolution().right_side_list([8,5,10,22,-14,12,5,8])) # [22,22,22,12,12,8,8,-1]
print(ReplaceElementsSolution().right_side_list([1,2,3,4,5,6,7,8,9,10])) # [10,10,10,10,10,10,10,10,10,-1]
print()



# Two Sum
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target. You may assume that each input would have exactly
# one solution, and you may not use the same element twice.

class TwoSumSolution:
    """
    Class to find the indices of two numbers that add up to a specific target.
    """

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the indices of two numbers that add up to a specific target.

        Args:
            nums (List[int]): The input array of numbers.
            target (int): The target sum.

        Returns:
            List[int]: The indices of the two numbers that add up to the target.
        """
        # Create a dict to store the indices of the numbers.
        num_dict = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                # If the two numbers add up to the target, return their indices.
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        # If no solution is found, return an empty list.
        return []


print(TwoSumSolution().two_sum([2,7,11,15], 9)) # [0,1]
print(TwoSumSolution().two_sum([3,2,4], 6)) # [1,2]
print(TwoSumSolution().two_sum([3,3], 50)) # []
print(TwoSumSolution().two_sum([1,2,3,4,5,6,7,8,9,10], 19)) # [8,9]
print()

