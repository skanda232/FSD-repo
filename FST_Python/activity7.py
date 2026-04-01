list1 = [10, 21, 4, 45, 66, 93]
list2 = [11, 22, 33, 44, 55, 66]

# Get odd numbers from list1
odd_numbers = [num for num in list1 if num % 2 != 0]

# Get even numbers from list2
even_numbers = [num for num in list2 if num % 2 == 0]

# Combine both lists
new_list = odd_numbers + even_numbers

print(new_list)