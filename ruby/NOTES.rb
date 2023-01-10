# UNCOMPRESS
# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern: <number><char> for example, '2c' or '3a'.
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
      count = s[i..j].to_i
      count.times { result.push(s[j]) }
      j += 1
      i = j
    end
  end
  result.join('')
end

p 'UNCOMPRESS'
p uncompress("2c3a1t") # -> 'ccaaat'
p uncompress("4s2b") # -> 'ssssbb'
p uncompress("2p1o5p") # -> 'ppoppppp'
p uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
p uncompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
puts



puts
puts
p [1,2,3,4,5].map { |x| x * x }

# How to do a binary_search algorithm...

def binary_search(array, target)
  return "Target no found" if array.nil?
  middle_index = array.length / 2
  case target <=> array[middle_index]
  when -1
    left_side = binary_search(array.take(middle_index), target)
  when 0 
    return middle_index
  else
    right_side = binary_search(array.drop(middle_index + 1), target)
    right_side.nil? ? nil : (middle_index + 1) + right_side
  end
end

p binary_search([5,6,7,8,9], 9)


