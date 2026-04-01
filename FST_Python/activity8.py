
# Get tuple input from user
user_input = input("Enter numbers by spaces: ")
numbers = tuple(int, user_input.split())

print(f"Tuple: {numbers}")
print("Numbers divisible by 5:")

divisible_by_5 = [num for num in numbers if num % 5 == 0]

if divisible_by_5:
    for num in divisible_by_5:
        print(num)
else:
    print("No numbers divisible by 5 found.")