dict1 = eval(input("Enter the first dictionary: "))
dict2 = eval(input("Enter the second dictionary: "))

merged_dict = dict1.copy()
merged_dict.update(dict2)

print("The merged dictionary is:", merged_dict)
