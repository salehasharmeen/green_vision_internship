rows = 5

for i in range(1, rows + 1):
    # Print ascending part
    for j in range(1, i + 1):
        print(j, end=' ')
    # Print descending part
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    print()
