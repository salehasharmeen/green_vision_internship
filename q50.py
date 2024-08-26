import math

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

if denominator == 0:
    print("Denominator cannot be zero.")
else:
    gcd = math.gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    print(f"The simplified fraction is: {simplified_numerator}/{simplified_denominator}")
