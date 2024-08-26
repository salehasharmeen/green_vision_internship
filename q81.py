d = eval(input("Enter the dictionary: "))

min_key = min(d, key=d.get)
max_key = max(d, key=d.get)

d[min_key], d[max_key] = d[max_key], d[min_key]

print("The updated dictionary is:", d)
