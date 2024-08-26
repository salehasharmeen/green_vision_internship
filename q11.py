def simint():
    vp= int (input("Enter the value of principle:"))
    ri= int (input("Enter the rate of intrest:"))
    tp= int (input("Enter the time period:"))
    si=(vp*ri*tp)//100
    print("The value if simple intrest is ",si)
simint()