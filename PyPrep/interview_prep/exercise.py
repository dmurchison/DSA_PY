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
print(map_by_name(pets))  # ['Rolo', 'Sunny', 'Saki', 'Finn']
print(map_by_name(friends))  # ['Alice', 'Bob', 'Charlie']
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
print(map_by_key(locations, "city"))  # ['New York City', 'San Francisco', 'Portland']
print(map_by_key(locations, "state"))  # ['New York', 'California', 'Oregon']
print(map_by_key(locations, "coast"))  # ['East', 'West', 'West']
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
print(yell_sentence(sentence1)) # HELLO! WORLD!
print(yell_sentence(sentence2)) # I! LOVE! PYTHON!
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



print(whisper_words(["KEEP", "The", "NOISE", "DOwn"]))
print(whisper_words(["WHAT", "IS", "that", "nOIse?"]))
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

