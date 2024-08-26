list1 = list(map(int, input("Enter the first list items separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list items separated by spaces: ").split()))

merged_list = list1.copy()  # Create a copy of the first list

for item in list2:
    merged_list.append(item)

print("The merged list is:", merged_list)
