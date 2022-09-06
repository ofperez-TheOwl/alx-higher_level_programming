#!/usr/bin/node

const num1 = parseInt(process.argv[2], 10);
function factorial (num) {
  /* base case */
  if (isNaN(num) || num === 0) {
    return (1);
  }
  /* resursive instruction */
  return (num * factorial(num - 1));
}
console.log(factorial(num1));
