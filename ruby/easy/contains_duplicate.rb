# CONTAINS DUPLICATE:
# Given an array of integers, find if the array contains any duplicates.

require "set"
class Solution
  def contains_duplicate(nums)
    mySet = Set.new
    nums.each do |el|
      return true if mySet.include?(el)
      mySet.add(el)
    end
    return false
  end
end

a = Solution.new
p a.contains_duplicate([1,2,3,4,2])
p a.contains_duplicate([1,2,3,4])


