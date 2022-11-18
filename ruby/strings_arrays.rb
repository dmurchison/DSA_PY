# UNCOMPRESS
# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern: <number><char> for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(s)
  result = []
  numbers = '1234567890'
  i = 0
  j = 0
  while j < s.length
    if numbers.include?(s[j])
      j += 1
    else
      count = s[i..j].to_i
      count.times { result.push(s[j]) }
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
p uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
puts





# COMPRESS
# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences 
# of the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

def compress(s)
  result = []
  i = 0
  j = 0
  while j <= s.length
    if s[i] == s[j]
      j += 1
    else
      count = j - i
      count != 1 ? result.push(count.to_s + s[i]) : result.push(s[i])
      i = j
    end
  end
  return result.join('')
end

p 'COMPRESS'
p compress('ccaaatsss') # -> '2c3at3s'
p compress('ssssbbz') # -> '4s2bz'
p compress('ppoppppp') # -> '2po5p'
p compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
p compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); # -> '127y'
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





# INTERSECTION
# Write a function, intersection, that takes in two lists, a,b, as arguments. 
# The function should return a new list containing elements that are in both of the two lists.
# You may assume that each input list does not contain duplicate elements.
require 'set'

def intersection2(list1, list2)
  Set.new(list1) & Set.new(list2)
end

p 'INTERSECTION'
p intersection2([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
p intersection2([2,4,6], [4,2]) # -> [2,4]
p intersection2([4,2,1], [1,2,4,6]) # -> [1,2,4]
p intersection2([0,1,2], [10,11]) # -> []
a = Array (0..5000)
b = Array (0..5000)
p intersection2(a, b) # -> [0,1,2,3,..., 4999]
puts





# FIVE SORT
# Write a function, five_sort, that takes in a list of numbers as an argument. 
# The function should rearrange elements of the list such that all 5s appear at the end. 
# Your function should perform this operation in-place by mutating the original list. 
# The function should return the list.

# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.
# SUDO
# 

def five_sort(nums)
  i = 0
  j = nums.length - 1
  while i < j
    if nums[j] == 5
      j -= 1
    elsif nums[i] == 5
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else
      i += 1
    end
  end
  return nums
end

p 'FIVE SORT'

p five_sort([12, 5, 1, 5, 12, 7]) # -> [12, 7, 1, 12, 5, 5]
p five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]) # -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
p five_sort([5, 5, 5, 1, 1, 1, 4]) # -> [4, 1, 1, 1, 5, 5, 5]
p five_sort([5, 5, 6, 5, 5, 5, 5]) # -> [6, 5, 5, 5, 5, 5, 5]
p five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]) # -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
fours = [4] * 20000
fives = [5] * 20000
nums = fours + fives
# p five_sort(nums)
# twenty-thousand 4s followed by twenty-thousand 5s
# -> [4, 4, 4, 4, ..., 5, 5, 5, 5]







