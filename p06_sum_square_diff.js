/*Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.*/

function sumSquare(n) {
  let s = 0;
  for (let i = 1; i <= n; i++) {
    s += i;
  }
  return s ** 2;
}

function squareSum(n) {
  let s = 0;
  for (let i = 1; i <= n; i++) {
    s += i ** 2;
  }
  return s;
}

function sumSquareDifference(n) {
  return sumSquare(n) - squareSum(n);
}

console.log(sumSquareDifference(100));
