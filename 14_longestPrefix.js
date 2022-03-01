// Write a function to find the longest common prefix string
// amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"

// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""

const solution1 = (strList) => {
    // Time complexity = O(S) S= Suma de todos los caracteres en todas las cadenas 
    // space complexity = O(1)
  if (strList.length === 0) {
    return "";
  }
  let prefix = strList[0];
  for (i = 1; i < strList.length; i++) {
    while (strList[i].indexOf(prefix) != 0) {
      prefix = prefix.substring(0, prefix.length - 1);
      if (prefix.length === 0) return "";
    }
  }
  return prefix
};
let strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = ["acaro","caca"]
console.log(solution1(strs))