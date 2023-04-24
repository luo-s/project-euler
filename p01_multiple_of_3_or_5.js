// Find the sum of all the multiples of 3 or 5 below 1000. (natural numbers)
// Assume input is alway a natural number.

function multiplesOf3and5(number) {
  let sum = 0,
    i = 3;
  while (i < number) {
    if (i % 3 == 0 || i % 5 == 0) sum += i;
    i++;
  }
  return sum;
}

/* **********************  Oringinal solution   ********************/

function multiplesOf3and5(number) {
  let sum = 0;
  for (let i = 1; i < number; i++) {
    if (i % 15 == 0) {
      sum += i;
    } else if (i % 3 == 0) {
      sum += i;
    } else if (i % 5 == 0) {
      sum += i;
    }
  }
  return sum;
}

console.log(multiplesOf3and5(1000));
