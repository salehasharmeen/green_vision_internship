import math

numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
bin_size = int(input("Enter the bin size: "))

min_value = min(numbers)
max_value = max(numbers)

bins = range(min_value, max_value + bin_size, bin_size)
histogram = {bin_start: 0 for bin_start in bins}

for number in numbers:
    for bin_start in bins:
        if bin_start <= number < bin_start + bin_size:
            histogram[bin_start] += 1
            break

print("Histogram:", histogram)
