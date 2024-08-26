lst = list(map(int, input("Enter the list items separated by spaces: ").split()))

if not lst:
    print("The list is empty.")
else:
    max_item = lst[0]
    for item in lst:
        if item > max_item:
            max_item = item

    print("The maximum item in the list is:", max_item)
