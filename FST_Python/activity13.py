# def febonacci(n):
#     if n<=0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return febonacci(n-1) + febonacci(n-2)
# n = int(input("Enter the number of terms: "))
# print("Fibonacci sequence:")
# for i in range(n):
#     print(febonacci(i), end=" ")


def generate_fibonacci(n):
    fib_sequence = []
    
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

# Ask user for input
count = int(input("How many Fibonacci numbers do you want to generate? "))

# Generate and print the sequence
result = generate_fibonacci(count)
print("Fibonacci sequence:", result)