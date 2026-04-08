// import {} from "./activity/activity1.js";
import { generateFizzBuzz } from "./activity/activity2.js";
import { newBook } from "./activity/activity3.js";
import {numbers} from "./activity/activity4.js";  
import { appSettings } from "./activity/activity5.js";
import { Calculator } from "./activity/activity6.js";
import { demo } from "./activity/activity7.js";
import { getRoleDescription } from "./activity/activity8.js";
import { UserRole } from "./activity/activity8.js";
//activity 1
// console.log("Hello, World! This is a simple Node.js application.");

// //activity 2
// console.log(generateFizzBuzz(15));

// //activity 3
// console.log(newBook);

//activity 4
// console.log(numbers);

// activity 5
// console.log("appSettings function is ready to be used.")  ;
// appSettings({ theme: "light", fontSize: 16 });

//activity 6
// let calc = new Calculator();
// console.log(calc.add(5, 3)); // Output: 8
// console.log(calc.subtract(5, 3)); // Output: 2

//activity 7

// demo();

//activity 8
console.log(getRoleDescription(UserRole.Admin));
console.log(getRoleDescription(UserRole.User));
console.log(getRoleDescription(UserRole.Guest));


