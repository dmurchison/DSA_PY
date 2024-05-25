# LIST
# A list is a collection which is ordered and changeable.
# Allows duplicate members.

example_list = [1,2,3]

print(example_list)

example_list.append("Hello World") # type: ignore

print(example_list, type(example_list), len(example_list))
print()

# Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram
# of s. An anagram is when the two strings can be written using the exact same
# letters (so you can just rearrange the letters to get a different phrase or
# word).

class Anagrams:
    def is_anagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}
        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1
        return s_hash == t_hash

    

print(Anagrams().is_anagram("Hello", "NEVAA")) # False
print(Anagrams().is_anagram("anagram", "nagaram")) # True
print()


class Primeyz:
    def is_prime(self, n: int):
        if n <= 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

print(Primeyz().is_prime(7)) # True
print(Primeyz().is_prime(8)) # False

