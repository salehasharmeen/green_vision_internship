list1 = list(map(int, input("Enter the first list items separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list items separated by spaces: ").split()))

set1 = set(list1)
set2 = set(list2)

union_list = list(set1 | set2)
intersection_list = list(set1 & set2)

print("Union of the two lists:", union_list)
print("Intersection of the two lists:", intersection_list)
