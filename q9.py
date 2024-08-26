def triangle():
    a = int(input("Enter the first angle :"))
    b = int(input("Enter the second angle :"))
    c = int(input("Enter the third angle :"))
    if (a+b+c==180):
        print("These angles can form a triangle")
    else:
        print("These angles can't form a triangle")
triangle()
