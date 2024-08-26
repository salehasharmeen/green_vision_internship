total_sum = 0
count = 0

while True:
    number = float(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
    print("The sum of the numbers is:", total_sum)
    print("The average of the numbers is:", average)
else:
    print("No numbers were entered.")
