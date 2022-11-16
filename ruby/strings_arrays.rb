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
    end # concat j again and bring i up to speed
  end
  return result.join('') # join the result together and return it!
end

# UNCOMPRESS2
def uncompress2(s)
  result = []
  numbers = '0123456789'
  i = 0
  j = 0
  while j < s.length
    if numbers.include?(s[j])
      j += 1
    else
      s[i, j].to_i.times { result.push(s[j]) }
      j += 1
      i = j
    end
  end
  return result.join('')
end

p 'UNCOMPRESS'
p uncompress("2c3a1t") # -> 'ccaaat'
p uncompress("4s2b") # -> 'ssssbb'
p uncompress("2p1o5p") # -> 'ppoppppp'
p uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
p uncompress2("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
puts





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

# COMPRESS2
def compress2(s)
  result = []
  i = 0
  j = 0
  while j <= s.length
    if s[i] == s[j]
      j += 1
    else
      count = j - i
      result.push(count.to_s, s[i])
      i = j
    end
  end
  return result.join('')
end

p 'COMPRESS'
p compress2('ccaaatsss') # -> '2c3at3s'
p compress2('ssssbbz') # -> '4s2bz'
p compress2('ppoppppp') # -> '2po5p'
p compress2('nnneeeeeeeeeeeezz') # -> '3n12e2z'
p compress2('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); # -> '127y'
puts





# ANAGRAMS
# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2)
  return char_counter(s1) == char_counter(s2)
end
# helper
def char_counter(s)
  count = Hash.new(0)
  s.each_char do |el|
    count[el] += 1
  end
  return count
end

# ANAGRAMS2
def anagrams2(s1, s2)
  return char_counter2(s1) == char_counter2(s2)
end
# helper
def char_counter2(s)
  hash = Hash.new(0)
  s.each_char { |el| hash[el] += 1 }
  return hash
end

p 'ANAGRAMS'
p anagrams2('restful', 'fluster') # -> True
p anagrams2('cats', 'tocs') # -> False
p anagrams2('monkeyswrite', 'newyorktimes') # -> True
p anagrams2('paper', 'reapa') # -> False
p anagrams2('elbow', 'below') # -> True
p anagrams2('tax', 'taxi') # -> False
p anagrams2('taxi', 'tax') # -> False
p anagrams2('night', 'thing') # -> True
p anagrams2('abbc', 'aabc') # -> False
p anagrams2('po', 'popp') # -> False
p anagrams2('pp', 'oo') # -> False
puts





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

p 'MOST FREQUENT CHAR'
p most_frequent_char('bookeeper') # -> 'e'
p most_frequent_char('david') # -> 'd'
p most_frequent_char('abby') # -> 'b'
p most_frequent_char('mississippi') # -> 'i'
p most_frequent_char('potato') # -> 'o'
p most_frequent_char('eleventennine') # -> 'e'
p most_frequent_char('riverbed') # -> 'r'
puts





# PAIR SUM
# Write a function, pair_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a pair of indices whose elements sum to the given target. 
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair that sums to the target.

def pair_sum(numbers, target_sum)
  tuple = []
  numbers.each_with_index do |el1, idx1|
    numbers.each_with_index do |el2, idx2|
      return [idx1, idx2] if idx1 < idx2 && el1 + el2 == target_sum
    end
  end
  return nil
end

p 'PAIR SUM'
p pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
p pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
p pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
p pair_sum([1, 6, 7, 2], 13) # -> (1, 2)
p pair_sum([9, 9], 18) # -> (0, 1)
p pair_sum([6, 4, 2, 8 ], 12) # -> (1, 3)
puts





# PAIR PRODUCT
# Write a function, pair_product, that takes in a list and a target product as arguments. 
# The function should return a tuple containing a pair of indices whose elements multiply to the given target. 
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair whose product is the target.

def pair_product(numbers, target_product)
  numbers.each_with_index do |el1, idx1|
    numbers.each_with_index do |el2, idx2|
      return [idx1, idx2] if idx1 < idx2 && el1 * el2 == target_product
    end
  end
  return nil
end

p 'PAIR PRODUCT'
p pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
p pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
p pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)
p pair_product([4, 7, 9, 2, 5, 1], 35) # -> (1, 4)
p pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
p pair_product([4, 6, 8, 2], 16) # -> (2, 3)
puts








