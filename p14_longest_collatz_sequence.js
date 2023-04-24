/*The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Which starting number, under one million, produces the longest chain?*/

function sequenceLength(num) {
  let s = 0;
  function collatzSequence(num) {
    if (num === 1) {
      s += 1;
      return s;
    } else if (num % 2 === 0) {
      s += 1;
      return collatzSequence(num / 2);
    } else if (num % 2 === 1) {
      s += 1;
      return collatzSequence(num * 3 + 1);
    }
  }
  return collatzSequence(num);
}

function longestCollatzSequence(limit) {
  let l = 0;
  let number = 1;
  for (let i = Math.floor(limit / 2); i < limit; i++) {
    if (sequenceLength(i) > l) {
      l = sequenceLength(i);
      number = i;
    }
  }
  return number;
}

console.log(longestCollatzSequence(1000000));
