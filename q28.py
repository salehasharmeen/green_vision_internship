def is_prime():
    n = int(input("Enter a number: "))
    
    if n < 2:
        print(n, "is not a prime number")
        return
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            return
    
    print(n, "is a prime number")

is_prime()
