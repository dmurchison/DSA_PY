# frozen_string_literal: true

# class Solution
class Solution

  def self.contains_duplicate(nums)
    hash = Hash.new(0)
    nums.each do |el|
      return true if hash.key?(el)

      hash[el] += 1
    end
    false
  end

  def self.anagram?(str, tst)
    # binding.irb
    return false if str.length != tst.length

    hash_s = Hash.new(0)
    hash_t = Hash.new(0)
    i = 0
    while i < str.length
      hash_s[str[i]] += 1
      hash_t[tst[i]] += 1
      i += 1
    end
    hash_s == hash_t
  end

  def self.right_side(nums)
    right_max = -1
    i = nums.length - 1
    while i >= 0
      new_max = [right_max, nums[i]].max
      nums[i] = right_max
      right_max = new_max
      i -= 1
    end
    nums
  end

end

def prime_nums(num)
  return false if num < 2

  (2...num).each do |i|
    return false if (i % num).zero?
  end
  true
end

p prime_nums(2) # true
p prime_nums(3) # true
p prime_nums(4) # false
p prime_nums(5) # true
p Solution.contains_duplicate([1, 2, 3, 4, 3, 55]) # true
puts

p Solution.anagram?("racecar", "rcaegmxss") # false
p Solution.anagram?("anagram", "nagaram") # true
puts

p Solution.right_side([12, 22, 4, 1, 8, 6, 5]) # [22,8,8,8,6,5,-1]
