def multiply():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    
    result = 0
    for _ in range(abs(b)):
        result += a
    
    if b < 0:
        result = -result
    
    print("The result of multiplication is", result)

multiply()
