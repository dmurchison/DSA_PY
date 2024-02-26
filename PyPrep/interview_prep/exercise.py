from typing import Union
# Exercises

# Map by name
# Write a function that takes in an array of hashes and returns a new array
# containing the "name" of each hash.

def map_by_name(arr) -> list[str]:
    """
    Given an array of hashes, return a new array containing the "name" of each hash.
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
print(whisper_words(["WHAT", "IS", "that", "nOIse?"])) # ->  ["what...", "is...", "that...", "noise?..."]
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

print(o_words(sentence1)) # ['Hello', 'World']
print(o_words(sentence2)) # ['love', 'Python']
print(o_words("nOthing is that great")) # ['nOthing']
print(o_words("This is great")) # ["This sentence does not contain any o's"]
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

print(last_index("Hellooo", "R")) # The string "Helloooo" does not contain any "R"
print(last_index("abca", "A")) # 3
print(last_index("mississipi", "i")) #  9
print(last_index("octagon", "o")) #=> 5
print(last_index("programming", "m")) #=> 7
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



print(prime_checker(2)) #=> true
print(prime_checker(5)) #=> true
print(prime_checker(11)) #=> true
print(prime_checker(4)) #=> false
print(prime_checker(9)) #=> false
print(prime_checker(-5)) #=> false


