def compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time)

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in decimal form): "))
time = float(input("Enter the time in years: "))
n = int(input("Enter the number of times interest is compounded per year: "))

amount = compound_interest(principal, rate, time, n)
print("The compound interest is:", amount - principal)
