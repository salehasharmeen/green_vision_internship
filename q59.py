string = input("Enter the string: ")

title_case = ' '.join(word.capitalize() for word in string.split())

print("Title case string:", title_case)
