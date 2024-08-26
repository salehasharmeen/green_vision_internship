lst = list(map(int, input("Enter the list items separated by spaces: ").split()))

is_ascending = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

if is_ascending:
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
