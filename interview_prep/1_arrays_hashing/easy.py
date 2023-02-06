from typing import List


# EASY PROBLEMS


# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False

    def contains_duplicate_2(self, nums: List[int]) -> bool:
        print(len(set(nums)))
        print(len(nums))


print(Solution().contains_duplicate_2([1,2,3,1])) # True
print(Solution().contains_duplicate_2([1,2,3,4])) # False
print()
print(Solution().contains_duplicate([1,2,3,1])) # True
print(Solution().contains_duplicate([1,2,3,4])) # False
print(Solution().contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
print(Solution().contains_duplicate([1,2,3,4,5,6,7,8,9,10])) # False
print(Solution().contains_duplicate([1,1,1,1,1,1,1,1,1,1])) # True
print(Solution().contains_duplicate([1,1,2,2])) # True
print()



# Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram
# of s.

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        for c in t:
            if c not in hash_map:
                return False
            hash_map[c] -= 1
            if hash_map[c] < 0:
                return False
        return True

print(Solution().is_anagram("anagram", "nagaram")) # True
print(Solution().is_anagram("rat", "car")) # False
print(Solution().is_anagram("a", "ab")) # False
print(Solution().is_anagram("ab", "a")) # False
print(Solution().is_anagram("aacc", "ccac")) # False
print(Solution().is_anagram("racecar", "racecar")) # True
print()





