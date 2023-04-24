/*Starting in the top left corner of a 2×2 grid, and only being able to 
move to the right and down, there are exactly 6 routes to the bottom 
right corner.
How many such routes are there through a 20×20 grid?*/

//This is a question to compute combination(2n, n)

function factorial(num) {
  if (typeof num !== "number" || num < 1) {
    return "not a valid natural number";
  }
  let fac = 1;
  while (num > 0) {
    if (num === 1) {
      return fac;
    } else {
      num -= 1;
      return (num + 1) * factorial(num);
    }
  }
  return fac;
}

function permutation(n, r) {
  return factorial(n) / factorial(n - r);
}

function combination(n, r) {
  return factorial(n) / (factorial(r) * factorial(n - r));
}

console.log(combination(40, 20));
