// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

// For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right.
// However, the numeral for four is not IIII. Instead, the number four is written
// as IV. Because the one is before the five we subtract it making four.
// The same principle applies to the number nine, which is written as IX. There
// are six instances where subtraction is used:

//     I can be placed before V (5) and X (10) to make 4 and 9.
//     X can be placed before L (50) and C (100) to make 40 and 90.
//     C can be placed before D (500) and M (1000) to make 400 and 900.

// Given an integer, convert it to a roman numeral.

// Input: num = 58
// Output: "LVIII"
// Explanation: L = 50, V = 5, III = 3.

// Input: num = 1994
// Output: "MCMXCIV"
// Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

const solution1 = (num, letter = "") => {
  let word = letter;
  switch (true) {
    case num >= 1000:
      console.log("1000");
      return word + solution1(num - 1000, "M");
    case num >= 900:
      console.log("900");
      return word + solution1(num - 900, "CM");
    case num >= 500:
      console.log("500");
      return word + solution1(num - 500, "D");
    case num >= 400:
      console.log("400");
      return word + solution1(num - 400, "CD");
    case num >= 100:
      console.log("100");
      return word + solution1(num - 100, "C");
    case num >= 90:
      console.log("90");
      return word + solution1(num - 90, "XC");
    case num >= 50:
      console.log("50");
      return word + solution1(num - 50, "L");
    case num >= 40:
      console.log("40");
      return word + solution1(num - 40, "XL");
    case num >= 10:
      console.log("10");
      return word + solution1(num - 10, "X");
    case num >= 9:
      console.log("9");
      return word + solution1(num - 9, "IX");
    case num >= 5:
      console.log("5");
      return word + solution1(num - 5, "V");
    case num >= 4:
      return word + solution1(num - 4, "IV");
    case num > 0:
      console.log("1");
      return word + solution1(num - 1, "I");
    default:
      return letter;
  }
};

const solution2 = (num) => {

  const letters = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I",
  ];
  const numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

  let ptr = 0;
  let str = "";

  while (num) {
    if (num >= numbers[ptr]) {
      str += letters[ptr];
      num -= numbers[ptr];
    } else {
      ptr++;
    }
  }
  return str
};

const solution3 = (num) => {
  const tokenize = (num,char1,char5,char10) => {
    word = ""
    if(num<=0 || num>=10) return word
    if(num===9) word = char1+char10
    else if(num>=5) word = char5+char1.repeat(num-5)
    else if(num==4) word = char1+char5
    else word = char1.repeat(num)
    return word

  }
  word = ""
  thousands = (num/1000)>>0 // division entera
  if(thousands>0){
    word = word + "M".repeat(thousands)
  }
  num = num % 1000
  hundreds = (num/100)>>0
  word = word + tokenize(hundreds,'C','D','M')
  
  num = num % 100
  tens = (num/10)>>0
  word = word + tokenize(tens,'X','L','C')

  num = num % 10
  word = word + tokenize(num,'I','V','X')
  return word

}

let num = 58;
num = 1994;
num = 1900;
console.log(solution3(3));
