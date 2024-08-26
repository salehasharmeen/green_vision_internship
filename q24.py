def sum_of_n_numbers():
    n = int(input("Enter the value of n: "))
    
    sum_n = n * (n + 1) // 2
    
    print("The sum of the first", n, "numbers is", sum_n)

sum_of_n_numbers()
