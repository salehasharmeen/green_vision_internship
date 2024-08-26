def profit():
    costpr = int(input("Enter the cost price : "))
    sellpr = int(input("Enter the selling price : "))
    if(costpr<sellpr):
        print("You're in profit")
    else:
        print("You're in loss")
profit()