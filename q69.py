lst = list(map(int, input("Enter the list items separated by spaces: ").split()))
item_to_replace = int(input("Enter the item to replace: "))
replacement_item = int(input("Enter the replacement item: "))

for i in range(len(lst)):
    if lst[i] == item_to_replace:
        lst[i] = replacement_item

print("The updated list is:", lst)
