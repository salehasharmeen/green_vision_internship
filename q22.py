def animals():
    heads = int(input("Enter the total number of heads: "))
    legs = int(input("Enter the total number of legs: "))
    
    chickens = (2 * heads - legs // 2)
    dogs = heads - chickens
    
    if chickens < 0 or dogs < 0 or chickens % 1 != 0 or dogs % 1 != 0:
        print("No solution possible with the given heads and legs")
    else:
        print("The number of chickens is", int(chickens))
        print("The number of dogs is", int(dogs))

animals()
