from typing import List

# Easy Array Hashing Problems

class DuplicateSolution:
    def contains_dup(self, nums: List[int]) -> bool:
        set_checker = set()
        for n in nums:
            if n in set_checker:
                return True
            set_checker.add(n)
        return False

print(DuplicateSolution().contains_dup([1,2,3,3,4,5]))
print(DuplicateSolution().contains_dup([1,2,3,4,5]))

class Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s, hash_t = {}, {}
        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        return hash_s == hash_t

print(Anagram().isAnagram("anagram", "nagaram"))

