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
      i += 1
    end
    return hashS == hashT
  end

end



p Solution.contains_duplicate([1,2,3,4,3,55]) # true


p Solution.is_anagram("racecar", "rcaegmxss") # false
p Solution.is_anagram("anagram", "nagaram") # true