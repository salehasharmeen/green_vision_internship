lst = list(map(int, input("Enter the list items separated by spaces: ").split()))

n = len(lst)

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted list:", lst)
