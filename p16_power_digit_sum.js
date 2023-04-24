/* 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000? */

//key is suppress scientific notation for large number JS: BigInt.

function powerDigitSum(exponent) {
  // Take exponent and convert to string of digits
  const num = BigInt(Math.pow(2, exponent));
  const digits = num.toString().split("");
  // Sum digits in string representation
  return digits.reduce((sum, digit) => sum + parseInt(digit), 0);
}
