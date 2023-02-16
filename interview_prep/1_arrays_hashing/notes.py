

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




class Solution:
    def right_side_list(self, arr: list) -> list:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr


print(Solution().right_side_list([1,12,3,5,-5,2])) # [12,5,5,2,2,-1]
print(Solution().right_side_list([8,5,10,22,-14,12,5,8])) # [22,22,22,12,12,8,8,-1]
print()


class Solution:
    def two_sum(self, nums: list, target: int) -> list:
        myMap = {}
        for i, el in enumerate(nums):
            diff = target - el
            if diff in myMap:
                return [myMap[diff], i]
            myMap[el] = i


print(Solution().two_sum([1,2,2,5,8], 6)) # [0,3]
print(Solution().two_sum([4,2,9,6,3], 12)) # [2,4]
print()
