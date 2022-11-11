def greet(s)
  return 'hey ' + s
end

p greet("Duncan") # -> "hey Duncan"

def max_value(nums)
  nums.max
end

p max_value([4,7,2,8,10,9]) # -> 10

def is_prime(n)
  return false if n < 2
  (2...n).each do |i|
    return false if n % i == 0
  end
  return true
end

p is_prime(2) # -> True
p is_prime(3) # -> True
p is_prime(4) # -> False
p is_prime(5) # -> True
p is_prime(6) # -> False
p is_prime(7) # -> True
p is_prime(8) # -> False
p is_prime(25) # -> False
p is_prime(31) # -> True
p is_prime(2017) # -> True
p is_prime(2048) # -> False
p is_prime(1) # -> False
p is_prime(713) # -> False

