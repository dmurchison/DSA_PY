

class Solution:
    # def contains_duplicate(self, nums: list) -> bool:
    #     # Since the set doesn't contain any duplicates, I can check by simply
    #     # creating a set from the array and comparing them.
    #     return len(set(nums)) != len(nums)
    

    # I think this algorithm is a little faster because the code will stop iterating
    # and return True if after it finds the first match.
    def contains_duplicate(self, nums: list) -> bool:
        numSet = set()
        for i in nums:
            if i in numSet:
                return True
            numSet.add(i)
        return False


print(Solution().contains_duplicate([1,2,3,4,1,7])) # True
print(Solution().contains_duplicate([1,2,3,4,5])) # False
print(Solution().contains_duplicate([1,2,3,1])) # True
print(Solution().contains_duplicate([1,2,3,4])) # False
print(Solution().contains_duplicate([1,1,1,3,3,4,3,2,4,2])) # True
print(Solution().contains_duplicate([1,2,3,4,5,6,7,8,9,10])) # False
print(Solution().contains_duplicate([1,1,1,1,1,1,1,1,1,1])) # True
print(Solution().contains_duplicate([1,1,2,2])) # True
print()


class Solution:
    def is_anagram_slow(self, s: str, t: str) -> bool:
        hashS = {}
        for char in s:
            hashS[char] = 1 + hashS.get(char, 0)
        hashT = {}
        for char in t:
            hashT[char] = 1 + hashT.get(char, 0)
            
        return hashS == hashT


# This version is far more efficient because we are only iterating through ONE
# of the strings ONE time.
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        return hashS == hashT


print(Solution().is_anagram_slow("anagram", "nagaram")) # True
print(Solution().is_anagram_slow("rat", "car")) # False
print(Solution().is_anagram_slow("a", "ab")) # False
print(Solution().is_anagram_slow("ab", "a")) # False
print(Solution().is_anagram_slow("aacc", "ccac")) # False
print(Solution().is_anagram_slow("racecar", "racecar")) # True
print()
