string = input("Enter the string: ")
character = input("Enter the character to find: ")

index = string.find(character)

if index != -1:
    print(f"The index position of '{character}' is:", index)
else:
    print(f"'{character}' is not found in the string.")
