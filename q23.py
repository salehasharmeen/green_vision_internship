def swap():
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    
    # Swapping the values
    temp = a
    a = b
    b = temp
    
    print("After swapping:")
    print("The 1st number is", a)
    print("The 2nd number is", b)

swap()
