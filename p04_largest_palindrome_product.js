/*A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.*/
function isPalindrome(x) {
  return x === Number(x.toString().split("").reverse().join(""));
}

function largestPalindromeProduct(n) {
  let lp = 0;
  for (let i = 10 ** (n - 1); i < 10 ** n; i++) {
    for (let j = 10 ** (n - 1); j < 10 ** n; j++) {
      if (isPalindrome(i * j) && i * j > lp) {
        lp = i * j;
      }
    }
  }
  return lp;
}

console.log(largestPalindromeProduct(3));
