/*find the nth prime number*/

function isPrime(num) {
  for (let i = 2; i <= Math.ceil(num / 2); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function nthPrime(n) {
  let i = 2;
  let c = 0;
  while (true) {
    if (isPrime(i)) c++;
    if (c === n) return i;
    i++;
  }
}

console.log(nthPrime(10001));
