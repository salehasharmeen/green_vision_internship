x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
series_sum = 1

for i in range(2, n + 1):
    series_sum += (x ** i) / i

print("The sum of the series is:", series_sum)
