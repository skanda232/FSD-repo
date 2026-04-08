// function greet(name: string, age: number): string {
//   // Type validation
//   if (typeof name !== "string") {
//     throw new Error("Name must be a string");
//   }

//   if (typeof age !== "number") {
//     throw new Error("Age must be a number");
//   }

//   // Template literal
//   return `Hello ${name}, you are ${age} years old!`;
// }

// // Example usage
// console.log(greet("Skanda", 21));


let calcYear = (name: string, age: number): string => {
    let year100: number = (2026 - age)+100
    return `${name} will turn 100 years old in the year ${year100}`
}

console.log(calcYear("Skanda", 21));