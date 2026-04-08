function generateFizzBuzz(limit: number) {
    //Result array
    const result: string[] = [];

    //check number divisibility
    for (let i = 1; i <= limit; i++) {

        if (i % 3 === 0 && i % 5 === 0) {
            result.push("FizzBuzz");
        } else if (i % 3 === 0) {
            result.push("Fizz");
        } else if (i % 5 === 0) {
            result.push("Buzz");
        } else {
            result.push(i.toString());
        }
    }
    return result;
}

export{ generateFizzBuzz };