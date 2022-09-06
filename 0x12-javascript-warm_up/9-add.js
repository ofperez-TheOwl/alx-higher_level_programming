#!/usr/bin/node

const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);
function add (a, b) {
  return (a + b);
}
console.log(add(num1, num2));
/*
if (isNaN(num1) || (isNaN(num2))) {
  console.log('NaN');
} else {
  console.log(`${num1 + num2}`);
}
*/
