old_list = list(map(int, input("Enter the list items separated by spaces: ").split()))

new_list = [item ** 2 for item in old_list]

print("The new list with squared items is:", new_list)
