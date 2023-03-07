require 'set'

class Solution
  def initialize(nums)
    @nums = nums
  end
  def contains_duplicate(nums)
    nums.each do |num|
      my_set = Set.new
      return true if my_set.include?(num)
    end
    reutrn false
  end
end

s = Solution.new([1,2,3,4,5,6,7,8,9,10])
s.contains_duplicate

