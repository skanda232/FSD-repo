while True:
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        if numbers:
            print(f"List: {numbers}")
            print(f"Sum: {sum(numbers)}")
            print(f"Average: {sum(numbers)/len(numbers):.2f}\n")
        else:
            print("No numbers entered! Try again.\n")
    except ValueError:
        print("Invalid input! Please enter valid numbers separated by spaces.\n")
    
    if input("Calculate another sum? (yes/no): ").lower() != "yes":
        break
    