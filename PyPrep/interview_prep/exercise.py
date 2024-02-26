from operator import le
from typing import Union

# Exercises



# Map by name
# Write a function that takes in an array of hashes and returns a new array
# containing the "name" of each hash.

def map_by_name(arr) -> list[str]:
    """
    Given an array of hashes, return a new array containing the "name" of each
    hash.
    """
    # Create an array to store the names
    names = []
    for i in range(len(arr)):
        names.append(arr[i]["name"])
    return names


pets = [
    {"type": "dog", "name": "Rolo"},
    {"type": "cat", "name": "Sunny"},
    {"type": "rat", "name": "Saki"},
    {"type": "dog", "name": "Finn"}
]
friends = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print(map_by_name(pets))  # -> ['Rolo', 'Sunny', 'Saki', 'Finn']
print(map_by_name(friends))  # -> ['Alice', 'Bob', 'Charlie']
print()



# Map by key
# Write a function that takes in an array of hashes and a key name and returns a new
# array containing the value of each hash for the given key.

def map_by_key(arr, key) -> list:
    """
    Given an array of hashes and a key name, return a new array containing the
    value of each hash for the given key.
    """
    return [i[key] for i in arr]


locations = [
    {"city": "New York City", "state": "New York", "coast": "East"},
    {"city": "San Francisco", "state": "California", "coast": "West"},
    {"city": "Portland", "state": "Oregon", "coast": "West"}
]
print(map_by_key(locations, "city")) # -> ['New York City', 'San Francisco', 'Portland']
print(map_by_key(locations, "state")) # -> ['New York', 'California', 'Oregon']
print(map_by_key(locations, "coast")) # -> ['East', 'West', 'West']
print()



# Yell sentence
# Write a function that takes in a sentence string and returns a new sentence
# where every word is capitalized and followed by an exclamation point.

def yell_sentence(sent) -> str:
    """
    Given a sentence string return a new sentence where every word is
    capitalized and followed by an exclamation point.
    """
    # First, split the sentence into words
    words = sent.split()
    # Then, capitalize each word
    for i in range(len(words)):
        words[i] = words[i].upper() + "!"
    # Finally, join the words into a sentence
    return " ".join(words)


sentence1 = "Hello World"
sentence2 = "I love Python"
print(yell_sentence(sentence1)) # -> HELLO! WORLD!
print(yell_sentence(sentence2)) # -> I! LOVE! PYTHON!
print()



# Write a method whisper_words that takes in an array of words and returns a
# new array containing a whispered version of each word. See the examples.

def whisper_words(arr) -> list:
    """
    Return a new array that contains the same words all lowercase and followed
    by ...
    """
    final_arr = []
    for str in arr:
        final_arr.append(str.lower() + "...")
    return final_arr


print(whisper_words(["KEEP", "The", "NOISE", "DOwn"])) # -> ["keep..", "the...", "noise...", "down..."]
print(whisper_words(["WHAT", "IS", "that", "nOIse?"])) # -> ["what...", "is...", "that...", "noise?..."]
print()



# O Words
# Write a method o_words that takes in a sentence string and returns an array of
# the words that contain an "o".

def o_words(sent) -> list:
    """
    Return an array containing all of the words in the sentence that have a
    letter "o" in it.
    """
    final_arr = []
    checker = ["o", "O"]
    words = sent.split()
    for word in words:
        if any(el in word for el in checker):
            final_arr.append(word)
    if not final_arr:
        return ["This sentence does not contain any o's"]
    return final_arr


print(o_words(sentence1)) # -> ['Hello', 'World']
print(o_words(sentence2)) # -> ['love', 'Python']
print(o_words("nOthing is that great")) # -> ['nOthing']
print(o_words("This is great")) # -> ["This sentence does not contain any o's"]
print()



# Last Index
# Write a method last_index that takes in a string and a character. The method
# should return the last index where the character can be found in the string.

def last_index(string: str, char: str) -> Union[str, int]:
    """
    Return the last index where the char can be found in the string, if there is
    no char in the string, return 100
    """
    for i in reversed(range(len(string))):
        if string[i].lower() == char.lower():
            return i
    return f"The string '{string}' does not include an '{char}'"

print(last_index("Hellooo", "R")) # -> The string "Helloooo" does not contain any "R"
print(last_index("abca", "A")) # -> 3
print(last_index("mississipi", "i")) # -> 9
print(last_index("octagon", "o")) # -> 5
print(last_index("programming", "m")) # -> 7
print()



# Most Vowels
# Write a method most_vowels that takes in a sentence string and returns the
# word of the sentence that contains the most vowels.

def most_vowels(sentence) -> str:
    """
    Return the word in the sentence that contains the most vowels
    """
    # First setup a set to reference each unique vowel.
    vowels = set("aeiou")
    # Split the sentence into a words array.
    words = sentence.split()
    # Set a var to hold the maximums of each.
    max_vowels = 0
    max_words = []
    # Iterate through the words array.
    for word in words:
        # Use the sum method to easily count upwards by one each time a vowel is
        # spotted in a word.
        count = sum(1 for char in word if char.lower() in vowels)
        # After each word, check and update the new max_vowels and max_word
        # values.
        if count > max_vowels:
            max_vowels = count
            # This will start a new list with current word.
            max_words = [word]
        # If theres have another word with the same amount of vowels...
        elif count == max_vowels:
            # Append the word to the end of the max_words array.
            max_words.append(word)
    # Return the final values using string interpolation
    return f"{max_words}:{max_vowels}"


print(most_vowels("what a wonderful life")) # -> ['wonderful']:3
print(most_vowels("I can't WAIT until we go to NY!")) # -> ['WAIT']:2
print(most_vowels("SuPEr crowd today")) # -> ['SuPEr', 'today']:2
print()



# Prime?
# Write a method prime? that takes in a number and returns a boolean, indicating
# whether the number is prime. A prime number is only divisible by 1 and itself.

def prime_checker(num) -> bool:
    """
    Given an integer, return a boolean indicating whether or not the number is
    prime.
    """
    if num < 1 or num % 1 != 0 or num % num != 0:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


print(prime_checker(2)) # -> True
print(prime_checker(5)) # -> True
print(prime_checker(11)) # -> True
print(prime_checker(4)) # -> False
print(prime_checker(9)) # -> False
print(prime_checker(-5)) # -> False
print()



# Prime Numbers
# Write a method pick_primes that takes in an array of numbers and returns a new
# array containing only the prime numbers.

def prime_nums(numbers) -> list:
    """
    Write a method pick_primes that takes in an array of numbers and returns a
    new array containing only the prime numbers.
    """
    primes = []
    for num in numbers:
        if prime_checker(num):
            primes.append(num)
    return primes


print(prime_nums([1,2,3,4,5,6,7])) # -> [1,2,3,5,7]
print(prime_nums([-3,-1,5,6,7,8,9])) # -> [5,7]
print(prime_nums([6,7,8,9,10,11,12])) # -> [7,11]
print(prime_nums([13,14,15,16])) # -> [13]
print(prime_nums([4,6,8,14,15])) # -> []
print()



# Prime Factors
# Write a method prime_factors that takes in a number and returns an array
# containing all of the prime factors of the given number.

def prime_factors(num) -> list:
    """
    Write a method prime_factors that takes in a number and returns an array
    containing all of the prime factors of the given number.
    """
    # Find the factors and iterate to find the primes.
    factors = []
    for n in range(2, num+1):
        if num % n == 0:
            factors.append(n)
    return prime_nums(factors)


print(prime_factors(24)) # -> [2,3]
print(prime_factors(60)) # -> [2,3,5]
print(prime_factors(170)) # -> [2,5,17]
print()



# Greatest Factor Array
# Write a method greatest_factor_array that takes in an array of numbers and
# returns a new array where every even number is replaced with it's greatest
# factor. A greatest factor is the largest number that divides another with no
# remainder. For example the greatest factor of 16 is 8.

def greatest_factor(num) -> int:
    factors = []
    for n in range(1, num):
        if num % n == 0:
            factors.append(n)
    return max(factors)

def greatest_factor_arr(arr) -> list:
    """
    Return greatest factor of every even number, and if the number is odd just
    add it to the new array
    """
    final_arr = []
    for el in arr:
        if el % 2 == 0:
            final_arr.append(greatest_factor(el))
        else:
            final_arr.append(el)
    return final_arr


print(greatest_factor(16)) # -> 8
print(greatest_factor_arr([16, 7, 9, 14])) # -> [8, 7, 9, 7]
print(greatest_factor_arr([30, 3, 24, 21, 10])) # -> [15, 3, 12, 21, 5]
print()



# Perfect Square
# Write a method perfect_square? that takes in a number and returns a boolean
# indicating whether it is a perfect square. A perfect square is a number that
# results from multiplying a number by itself. For example, 9 is a perfect
# square because 3 * 3 = 9, 25 is a perfect square because 5 * 5 = 25.

def perfect_square(num) -> bool:
    """
    Return a bool indicating whether or not the input is a perfect square
    """
    res = False
    for n in range(1, num):
        if n * n == num:
            res = True
    return res


print(perfect_square(5)) # => False
print(perfect_square(12)) # => False
print(perfect_square(30)) # => False
print(perfect_square(9)) # => True
print(perfect_square(25)) # -> True



# Triple Sequence
# Write a method triple_sequence that takes in two numbers, start and length.
# The method should return an array representing a sequence that begins with
# start and is length elements long. In the sequence, every element should be 3
# times the previous element. Assume that the length is at least 1.

def triple_sequence(start_num: int, finish_length: int) -> list:
    """
    Given two integers, return an array that has a length of int2 and a starting
    element of int1. Every consecutive element should be 3x the previous.
    """
    # Create an array to append the new elements to.
    seq = [start_num]
    # Use a while loop to continue adding elements to the array while the length
    # is less than the finishing_length
    while len(seq) < finish_length:
        seq.append(seq[-1] * 3)
    return seq


print(triple_sequence(2, 4)) # -> [2, 6, 18, 54]
print(triple_sequence(4, 5)) # -> [4, 12, 36, 108, 324]
print()


# Summation Sequence
# A number's summation is the sum of all positive numbers less than or equal to
# the number. For example: the summation of 3 is 6 because 1 + 2 + 3 = 6, the
# summation of 6 is 21 because 1 + 2 + 3 + 4 + 5 + 6 = 21. Write a method
# summation_sequence that takes in a two numbers: start and length. The method
# should return an array containing length total elements. The first number of
# the sequence should be the start number. At any point, to generate the next
# element of the sequence we take the summation of the previous element. You can
# assume that length is not zero.

def summation_sequence(start: int, length: int) -> list:
    """
    Use summation seq to return a list that is "length" long and starts with
    "start"
    """
    seq = [start]
    while len(seq) < length:
        seq.append(sum(range(seq[-1] + 1)))
    return seq


print(summation_sequence(3, 4)) # => [3, 6, 21, 231]
print(summation_sequence(5, 3)) # => [5, 15, 120]
print()


# Fibonacci
# The fibonacci sequence is a sequence of numbers whose first and second
# elements are 1. To generate further elements of the sequence we take the sum
# of the previous two elements. For example the first 6 fibonacci numbers are
# 1, 1, 2, 3, 5, 8. Write a method fibonacci that takes in a number length and
# returns the fibonacci sequence up to the given length.

def fibonacci(length: int) -> list:
    """
    Return a list of the fibonacci sequence "length" long.
    """
    if length == 0:
        return []
    elif length == 1:
        return [1]
    seq = [1, 1]
    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])
    return seq

def fibonacci_rec(length):
    if length <= 0:
        return []
    elif length == 1:
        return [1]
    elif length == 2:
        return [1, 1]
    else:
        sequence = fibonacci_rec(length - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

print(fibonacci(0)) # => []
print(fibonacci_rec(0)) # => []
print(fibonacci(1)) # => [1]
print(fibonacci_rec(1)) # => [1]
print(fibonacci(6)) # => [1, 1, 2, 3, 5, 8]
print(fibonacci_rec(6)) # => [1, 1, 2, 3, 5, 8]
print(fibonacci(8)) # => [1, 1, 2, 3, 5, 8, 13, 21]
print(fibonacci_rec(8)) # => [1, 1, 2, 3, 5, 8, 13, 21]
print()


# Caesar Cipher
# Write a method caesar_cipher that takes in a string and a number. The method
# should return a new string where every character of the original is shifted
# num characters in the alphabet.

def caesar_cipher(string: str, num: int) -> str:
    alph = "abcdefghijklmnopqrstuvwxyz"
    final_str = ""
    for char in string:
        old_idx = alph.index(char)
        new_idx = old_idx + num
        new_char = alph[new_idx % len(alph)]
        final_str += new_char
    return final_str

print(caesar_cipher("apple", 1)) # -> "bqqmf"
print(caesar_cipher("bootcamp", 2)) # -> "dqqvecor"
print(caesar_cipher("zebra", 4)) # -> "difve"
print()


# Vowel Cipher
# Write a method vowel_cipher that takes in a string and returns a new string
# where every vowel becomes the next vowel in the alphabet.

def vowel_cipher(string):
    vowels = "aeiou"
    new_string = ""
    for char in string:
        if char in vowels:
            vowel_index = vowels.index(char)
            new_vowel = vowels[(vowel_index + 1) % len(vowels)]
            new_string += new_vowel
        else:
            new_string += char
    return new_string

print(vowel_cipher("bootcamp")) #=> buutcemp
print(vowel_cipher("paper cup")) #=> pepir cap

