def swap():
    a = int(input("Enter 1st number to swap : "))
    b = int(input("Enter 2nd number to swap : "))
    print("The numbers before swapping are : ",a,",",b)
    temp = a
    a = b
    b = temp 
    print("The numbers after swapping are : " ,a,",",b)
swap()