from typing import List


# EASY PROBLEMS
class DuplicateSolution:
    """
    Class to check if a list contains duplicate elements.
    """

    def contains_duplicate(self, nums: list) -> list:
        """
        Checks if the given list contains duplicate elements.

        Args:
            nums (list): The list of numbers to check.

        Returns:
            bool: True if the list contains duplicate elements, False otherwise.
        """
        return len(nums) != len(set(nums)) # type: ignore


# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

class Solution1:
    """
    Class representing a solution to the problem of checking for duplicates in an array.
    """

    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Checks whether the given array contains any duplicate elements.

        Args:
            nums (List[int]): The array of integers to be checked.

        Returns:
            bool: True if the array contains duplicates, False otherwise.
        """
        mySet = set()
        for i in nums:
            if i in mySet:
                return True
            mySet.add(i)
        return False


print(Solution1().contains_duplicate([1,2,3,1])) # True
print(Solution1().contains_duplicate([1,2,3,4])) # False
print(Solution1().contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
print(Solution1().contains_duplicate([1,2,3,4,5,6,7,8,9,10])) # False
print(Solution1().contains_duplicate([1,1,1,1,1,1,1,1,1,1])) # True
print(Solution1().contains_duplicate([1,1,2,2])) # True
print()



# Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram
# of s.

class Solution2:
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
        # First check if s and t strings are the same length.
        if len(s) != len(t):
            return False
        # Create two hashes to represent each string.
        hashS, hashT = {}, {}

        # Add values to the hashes by iterating through the length of the strings
        # and incrementing the values by 1.
        for i in range(len(s)):
            # Set the value of the current key to 1 + the original value of that key
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        # Now that we have two hash_counters representing each string, return this boolean.
        return hashS == hashT


print(Solution2().is_anagram("anagram", "nagaram")) # True
print(Solution2().is_anagram("rat", "car")) # False
print(Solution2().is_anagram("a", "ab")) # False
print(Solution2().is_anagram("ab", "a")) # False
print(Solution2().is_anagram("aacc", "ccac")) # False
print(Solution2().is_anagram("racecar", "racecar")) # True
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

