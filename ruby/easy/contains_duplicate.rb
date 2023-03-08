require 'set'
# require 'byebug'

class Solution
  def initialize(nums)
    @nums = nums
  end

  def contains_duplicate
    # debugger
    my_set = Set.new()
    @nums.each do |num|
      return true if my_set.include?(num)
      my_set.add(num)
    end
    return false
  end

end

s = Solution.new([1,2,3,4,5,6,7,8,9,10])
s1 = Solution.new([1,2,3,4,4,])
p s.contains_duplicate # false
p s1.contains_duplicate # true

