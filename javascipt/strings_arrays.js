// UNCOMPRESS
// Write a function, uncompress, that takes in a string as an argument. 
// The input string will be formatted into multiple groups according to the following pattern: <number><char> for example, '2c' or '3a'.
// The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. 
// You may assume that the input string is well-formed according to the previously mentioned pattern.

const uncompress = (s) => {
  let result = []; // final result array for time complexity (doesn't really matter in javascript bc strings are immutable)
  const numbers = '0123456789'; // to check my j variable
  let i = 0; // to track letters
  let j = 0; // to track numbers
  while (j < s.length) { // while j is in bounds
    if (numbers.includes(s[j])) {
      j += 1; // if s[j] is a number than just continue iterating
    } else {
      const num = Number(s.slice(i, j)); // once j is no longer a number, stop and slice the string from i to j and create a number of it.
      for (let count = 0; count < num; count += 1) {
        result.push(s[j]);
      } // iterate from 0 to that number and push that letter into the result on each iteration
      j += 1; 
      i = j; // bring i back to j and continue with the while loop
    }
  }
  return result.join(''); // once the while loop is done, turn the result back into a string and return it
};

console.log(uncompress("2c3a1t")); // -> 'ccaaat'
console.log(uncompress("4s2b")); // -> 'ssssbb'
console.log(uncompress("2p1o5p")); // -> 'ppoppppp'
console.log(uncompress("3n12e2z")); // -> 'nnneeeeeeeeeeeezz'
console.log(uncompress("127y")); // ->'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'


// COMPRESS
// Write a function, compress, that takes in a string as an argument. 
// The function should return a compressed version of the string where consecutive occurrences 
// of the same characters are compressed into the number of occurrences followed by the character. 
// Single character occurrences should not be changed.



