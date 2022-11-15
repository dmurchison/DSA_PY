# UNCOMPRESS
# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern: <number><char> for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(s)
  result = [] # setup array for the final result to be joined at the end of the end of the function
  numbers = '0123456789' # numbers string to test with the .include? method
  i = 0 # i will be the first pointer representing the first part of the number
  j = 0 # j will be the second pointer representing the second digit and the letter.
  while j < s.length # since j is the second pointer we will use this as the while loop
    if numbers.include?(s[j])
      j += 1 # if s[j] is a number than just concatonate
    else
      res = s.slice(i, j).to_i # else (once the j is on a letter) slice from i to j non inclusive and use the to_i method to change it to an integer
      res.times { result.push(s[j]) } # That number amount of times, push the letter (currently s[j]) into the result array created at the beginning of the function
      j += 1
      i = j
      # concat j again and bring i up to speed
    end
  end
  return result.join('') # join the result together and return it!
end

p uncompress("2c3a1t") # -> 'ccaaat'
p uncompress("4s2b") # -> 'ssssbb'
p uncompress("2p1o5p") # -> 'ppoppppp'
p uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
p uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'




# COMPRESS
# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences 
# of the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

def compress(s)
  result = [];
  i = 0;
  j = 0;
  while j <= s.length
    if s[i] == s[j]
      j += 1
    else
      count = j - i
      if count == 1
        result.push(s[i])
      else
        result.push(count, s[i])
      end
      i = j
    end
  end
  return result.join('')
end

p compress('ccaaatsss') # -> '2c3at3s'
p compress('ssssbbz') # -> '4s2bz'
p compress('ppoppppp') # -> '2po5p'
p compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
p compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); # -> '127y'




# ANAGRAMS
# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2)
  return char_counter(s1) == char_counter(s2)
end

def char_counter(s)
  count = Hash.new(0)
  s.each_char do |el|
    count[el] += 1
  end
  return count
end

p anagrams('restful', 'fluster') # -> True
p anagrams('cats', 'tocs') # -> False
p anagrams('monkeyswrite', 'newyorktimes') # -> True
p anagrams('paper', 'reapa') # -> False
p anagrams('elbow', 'below') # -> True
p anagrams('tax', 'taxi') # -> False
p anagrams('taxi', 'tax') # -> False
p anagrams('night', 'thing') # -> True
p anagrams('abbc', 'aabc') # -> False
p anagrams('po', 'popp') # -> False
p anagrams('pp', 'oo') # -> False




# MOST FREQUENT CHAR
# Write a function, most_frequent_char, that takes in a string as an argument. 
# The function should return the most frequent character of the string. 
# If there are ties, return the character that appears earlier in the string.

def most_frequent_char(s)
  hash = Hash.new(0)
  s.each_char do |el|
    hash[el] += 1
  end
  hash.max_by{ |k,v| v }[0]
end

p most_frequent_char('bookeeper') # -> 'e'
p most_frequent_char('david') # -> 'd'
p most_frequent_char('abby') # -> 'b'
p most_frequent_char('mississippi') # -> 'i'
p most_frequent_char('potato') # -> 'o'
p most_frequent_char('eleventennine') # -> 'e'
p most_frequent_char('riverbed') # -> 'r'





