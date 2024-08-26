original_list = list(map(int, input("Enter the list items separated by spaces: ").split()))

odd_numbers = [item for item in original_list if item % 2 != 0]
even_numbers = [item for item in original_list if item % 2 == 0]

print("List of odd numbers:", odd_numbers)
print("List of even numbers:", even_numbers)
