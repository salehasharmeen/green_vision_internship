def count_case_chars(s):
    counts = {'uppercase': 0, 'lowercase': 0}
    for char in s:
        if char.isupper():
            counts['uppercase'] += 1
        elif char.islower():
            counts['lowercase'] += 1
    return counts

# Example usage
string = input("Enter the string: ")
result = count_case_chars(string)
print("Character counts:", result)
