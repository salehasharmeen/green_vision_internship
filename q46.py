import math

n = int(input("Enter the value of n: "))
series_sum = 0

for i in range(1, n + 1):
    series_sum += i / math.factorial(i)

print("The sum of the series is:", series_sum)
