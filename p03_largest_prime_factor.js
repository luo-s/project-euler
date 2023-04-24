/*The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143? */

//prime number determinator
function isPrime(num) {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function largestPrimeFactor(num) {
  if (typeof num !== "number" || num < 1) {
    return console.log("not a valid natural number");
  } else {
    let lpf = -Infinity;
    if (isPrime(num)) {
      lpf = num;
    } else {
      for (let i = 1; i <= Math.ceil(Math.sqrt(num)); i++) {
        if (num % i === 0 && isPrime(i) && i > lpf) {
          lpf = i;
        }
      }
    }
    return lpf;
  }
}

console.log(largestPrimeFactor(13195));
console.log(largestPrimeFactor(600851475143));
