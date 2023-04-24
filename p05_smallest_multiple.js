/*2520 is the smallest number that can be divided by each of the number 
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?*/

//LCM of two numbers
function lcm(a, b) {
  return (a * b) / gcd(a, b);
}

//Euclidean recursive algorithm
function gcd(a, b) {
  if (b === 0) return a;
  return gcd(b, a % b);
}

function smallestMult(n) {
  let maxLCM = 1;
  //Getting the LCM in the range
  for (let i = 2; i <= n; i++) {
    maxLCM = lcm(maxLCM, i);
  }
  return maxLCM;
}

//**********************Original solution  *********************/
function isPrime(num) {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function primeList(num) {
  let list = [];
  for (let i = 2; i <= num; i++) {
    if (isPrime(i)) {
      list.push(i);
    }
  }
  return list;
}

function expList(num) {
  let list = primeList(num);
  let exp = [];
  for (let ele of list) {
    let i = 1;
    while (ele ** i <= num) {
      i++;
    }
    exp.push(i - 1);
  }
  return exp;
}

function smallestMult(n) {
  let prime = primeList(n);
  let exp = expList(n);
  let sm = 1;
  for (let i = 0; i < prime.length; i++) {
    sm *= prime[i] ** exp[i];
  }
  return sm;
}

console.log(smallestMult(20));
