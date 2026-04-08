const numbers = [1, 2, 3, 4, 5, 6];

const result = numbers
  .filter(num => num % 2 === 0)   // keep even numbers
  .map(num => num * num);         // square them

console.log(result);

export {numbers};