/* There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.*/

function specialPythagoreanTriplet(n) {
  for (let a = 1; a < n; a++) {
    for (let b = 1; b < n; b++) {
      if (a ** 2 + b ** 2 === (n - a - b) ** 2) {
        return a * b * (n - a - b);
      }
    }
  }

  return true;
}

console.log(specialPythagoreanTriplet(1000));
