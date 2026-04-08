class Calculator {
    private lastResult: number = 0;

    getResult(): number {
        return this.lastResult;
    }

    add (num1: number, num2: number): number {
        this.lastResult = num1 + num2;
        return this.lastResult;
    }

    subtract (num1: number, num2: number): number {
        this.lastResult = num1 - num2;
        return this.lastResult;
    }

    
    }


export { Calculator };