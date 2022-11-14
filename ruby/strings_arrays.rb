
# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:
# <number><char>
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def uncompress(s)
  result = []
  numbers = '0123456789'
  i = 0
  j = 0
  while j < s.length
    if numbers.include?(s[j])
      j += 1
    else
      res = s.slice(i, j).to_i
      res.times { result.push(s[j]) }
      j += 1
      i = j
    end
  end
  result.join('')
end

p uncompress("2c3a1t") # -> 'ccaaat'
p uncompress("4s2b") # -> 'ssssbb'
p uncompress("2p1o5p") # -> 'ppoppppp'
p uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
p uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'