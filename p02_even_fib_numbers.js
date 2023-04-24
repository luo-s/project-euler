/*By considering the terms in the Fibonacci sequence 
(1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...)
whose values do not exceed four million, find the sum of the even-valued terms.*/

//fibonacci generator
function fib(index) {
  let f = 0;
  if (index == 1) {
    f = 1;
  } else if (index == 2) {
    f = 2;
  } else {
    f = fib(index - 1) + fib(index - 2);
  }
  return f;
}

//find the index of the last fib number <= limit
function fibLessThan(limit) {
  let index = 1;
  while (fib(index) <= limit) {
    index++;
  }
  return index - 1;
}

// even numbers pop up every 3 count (2nd, 5th, 8th, ...)
function fiboEvenSum(n) {
  let sum = 0;
  for (let i = 2; i <= fibLessThan(n); i += 3) {
    sum += fib(i);
  }
  return sum;
}

console.log(fiboEvenSum(4000000));
