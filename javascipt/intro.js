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

module.exports = {
  maxValue,
};
maxValue([4, 7, 2, 8, 10, 9]); // -> 10
maxValue([10, 5, 40, 40.3]); // -> 40.3
maxValue([-5, -2, -1, -11]); // -> -1
maxValue([42]); // -> 42
maxValue([1000, 8]); // -> 1000
maxValue([1000, 8, 9000]); // -> 9000
maxValue([2, 5, 1, 1, 4]); // -> 5


