number = int(input("Enter a number: "))

factors = [i for i in range(1, number + 1) if number % i == 0]

print("The factors of", number, "are:", factors)
