/* Find the sum of all the primes below N (two million).*/
function isPrime(num) {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function primeSum(n) {
  let s = 0;
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      s += i;
    }
  }
  return s;
}

console.log(primeSum(17));
console.log(primeSum(2001));
console.log(primeSum(140759));
console.log(primeSum(2000000));
