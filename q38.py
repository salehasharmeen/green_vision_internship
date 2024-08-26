number = input("Enter a number: ")
num_digits = len(number) if number.isdigit() else len(number) - 1  # Adjust for negative sign

print("The number of digits is:", num_digits)
