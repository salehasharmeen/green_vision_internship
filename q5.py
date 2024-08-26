def reverse():
    n = int(input("Enter a four digit number: "))
    rev_num = 0
    original = n  
    
    for i in range(1, 5):
        print(n % 10, end="")  
        rev_num = rev_num * 10 + n % 10  # Form the reversed number
        n = n // 10      
    if rev_num == original:
        print("\nThe reverse is correct")

reverse()
