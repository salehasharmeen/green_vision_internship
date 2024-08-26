lst = list(map(int, input("Enter the list items separated by spaces: ").split()))
number_to_search = int(input("Enter the number to search: "))

if number_to_search in lst:
    print(f"{number_to_search} is in the list.")
else:
    print(f"{number_to_search} is not in the list.")

