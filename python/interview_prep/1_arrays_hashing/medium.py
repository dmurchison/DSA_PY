from typing import List

# MEDIUM PROBLEMS


# Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hash_map:
                hash_map[sorted_s].append(s)
            else:
                hash_map[sorted_s] = [s]
        return list(hash_map.values())

print(Solution().group_anagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution().group_anagrams([""])) # [[""]]
print(Solution().group_anagrams(["a"])) # [["a"]]
print(Solution().group_anagrams(["a", "a"])) # [["a", "a"]]
print(Solution().group_anagrams(["a", "b"])) # [["a"], ["b"]]
print(Solution().group_anagrams(["a", "b", "a"])) # [["a", "a"], ["b"]]
print(Solution().group_anagrams(["a", "b", "a", "b"])) # [["a", "a"], ["b", "b"]]
print(Solution().group_anagrams(["a", "b", "a", "b", "a"])) # [["a", "a", "a"], ["b", "b"]]
print()

