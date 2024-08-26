def is_narcissistic(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == number
number = int(input("Enter a number to check if it is an narcissistic number: "))
if is_narcissistic(number):
    print(f"{number} is an narcissistic number.")
else:
    print(f"{number} is not an narcissistic number.")
