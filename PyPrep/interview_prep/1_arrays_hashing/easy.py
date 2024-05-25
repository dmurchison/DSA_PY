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

