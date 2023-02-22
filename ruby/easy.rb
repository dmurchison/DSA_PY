require 'byebug'

class Solution

  def self.contains_duplicate(nums)
    hash = Hash.new(0)
    nums.each do |el|
      if hash.key?(el)
        return true
      end
      hash[el] += 1
    end
    false
  end

  def self.is_anagram(s, t)
    if s.length != t.length
      return false
    end
    hashS = Hash.new(0)
    hashT = Hash.new(0)
    i = 0
    while i < s.length
      hashS[s[i]] += 1
      hashT[t[i]] += 1
      debugger
      i += 1
    end
    return hashS == hashT
  end


  def self.right_side(nums)
    rightMax = -1
    i = nums.length - 1
    while i >= 0
      newMax = [rightMax, nums[i]].max
      nums[i] = rightMax
      rightMax = newMax
      i -= 1
    end
    return nums
  end

end

def prime_nums(n)
  if n < 2
    return false
  end
  (2...n).each do |i|
    if i % n == 0
      return false
    end
  end
  return true
end

p prime_nums(2) # true
p prime_nums(3) # true
p prime_nums(4) # false



p Solution.contains_duplicate([1,2,3,4,3,55]) # true
puts

p Solution.is_anagram("racecar", "rcaegmxss") # false
p Solution.is_anagram("anagram", "nagaram") # true
puts

p Solution.right_side([12,22,4,1,8,6,5]) 
