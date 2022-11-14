
# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:
# <number><char>
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.
# 2 POINTER METHOD
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