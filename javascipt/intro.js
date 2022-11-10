// Hey Programmer
// Write a function greet that takes in a string argument, s, and returns the string "hey s". No tricks here. Run the tests to check your work.

const greet = (s) => {
  // todo
  return "hey " + s; 
};

console.log(greet("alvin")); // -> 'hey alvin'
console.log(greet("jason")); // -> 'hey jason'
console.log(greet("how now brown cow")); // -> 'hey how now brown cow'



// Max Value
// Write a function, maxValue, that takes in array of numbers as an argument. The function should return the largest number in the array.
// Solve this without using any built-in array methods.
// You can assume that the array is non-empty.

const maxValue = (nums) => {
  // todo
  let max = -Infinity; // -Infinity is guaranteed to always be smaller than any other number
  for (let num of nums) { // (for of) loop will iterate through every element of an array, NOT the indeces
    if (num > max) {
      max = num;
    } // if num is greater than our max variable, then replace the max var with the number
  }
  return max // once finished iterating, return whichever number is left in that max variable
};

console.log(maxValue([4, 7, 2, 8, 10, 9])); // -> 10
console.log(maxValue([10, 5, 40, 40.3])); // -> 40.3
console.log(maxValue([-5, -2, -1, -11])); // -> -1
console.log(maxValue([42])); // -> 42
console.log(maxValue([1000, 8])); // -> 1000
console.log(maxValue([1000, 8, 9000])); // -> 9000
console.log(maxValue([2, 5, 1, 1, 4])); // -> 5



// isPrime
// Write a function, isPrime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.
// A prime number is a number that is only divisible by two distinct numbers: 1 and itself.
// For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.
// You can assume that the input number is a positive integer.

const isPrime = (n) => {
  if (n < 2) return false; // any number less than 2 CANNOT be a prime number
  for (let i = 2; i < n; i++) { // iterate from 2 up to n (no reason to check 1 or n)
    if (n % i === 0) return false; // if the number is divisible by any number between 2 and itself, return false
  }
  return true; // once the iteration is complete and false has still not been returned, we can finally return true
};

console.log(isPrime(2)); // -> true
console.log(isPrime(3)); // -> true
console.log(isPrime(4)); // -> false
console.log(isPrime(5)); // -> true
console.log(isPrime(6)); // -> false
console.log(isPrime(7)); // -> true
console.log(isPrime(8)); // -> false
console.log(isPrime(25)); // -> false
console.log(isPrime(31)); // -> true
console.log(isPrime(2017)); // -> true
console.log(isPrime(2048)); // -> false
console.log(isPrime(1)); // -> false
console.log(isPrime(713)); // -> false








