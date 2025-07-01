let num1 = 5;
let num2 = 10;
let sum1 = num1 + num2;
console.log("Sum:", sum1);


let number1 = 7;

if (number1 % 2 === 0) {
    console.log(number1 + " is Even");
} else {
    console.log(number1 + " is Odd");
}


for (let i = 1; i <= 5; i++) {
    console.log(i);
}



let str = "hello";
let reversed1 = str.split("").reverse().join("");
console.log("Reversed String:", reversed1);


for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {
        console.log(i + " is Even");
    } else {
        console.log(i + " is Odd");
    }
}



let num3 = 7;
let isPrime = true;

if (num3 === 1) {
    isPrime = false;
} else {
    for (let i = 2; i < num3; i++) {
        if (num3 % i === 0) {
            isPrime = false;
            break;
        }
    }
}

if (isPrime) {
    console.log(num3 + " is a Prime Number");
} else {
    console.log(num3 + " is NOT a Prime Number");
}


let a = 5;
let b = 10;

let temp1 = a;
a = b;
b = temp1;

console.log("After swapping: a =", a, "b =", b);


let x = 10, y = 20, z = 15;

if (x >= y && x >= z) {
    console.log("Largest:", x);
} else if (y >= x && y >= z) {
    console.log("Largest:", y);
} else {
    console.log("Largest:", z);
}

let num4 = 5;
let factorial = 1;

for (let i = 1; i <= num4; i++) {
    factorial *= i;
}

console.log("Factorial of", num4, "is", factorial);



let word = "racecar";
let reversed = word.split("").reverse().join("");

if (word === reversed) {
    console.log(word + " is a Palindrome");
} else {
    console.log(word + " is NOT a Palindrome");
}


let number = 1234;
let sum2 = 0;

while (number > 0) {
    sum2 += number % 10;
    number = Math.floor(number / 10);
}

console.log("Sum of digits is", sum2);


for (let i = 1; i <= 20; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}




let num = 153;
let sum = 0;
let temp = num;

while (temp > 0) {
    let digit = temp % 10;
    sum += digit ** 3;
    temp = Math.floor(temp / 10);
}

if (sum === num) {
    console.log(num + " is an Armstrong Number");
} else {
    console.log(num + " is NOT an Armstrong Number");
}

