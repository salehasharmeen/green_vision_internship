#def salary():
#    sal = int(input("Enter your salary : "))
 #   a = sal*100000
  #  hra = a%10
   # da=a%5
#    pf = a%3
 #   if(a>5 and a<10):
  #      tax=a%10
   # elif(a>11 and a<20):
    #    tax=a%20
#    elif(a>20):
 #       tax=a%30
  #  else:
   #     tax=print("k")
#    inhand= a-hra-da-pf-tax
 #   print("Your in hand salary is ",inhand)
#salary()
def salary():
    a = int(input("Enter your salary in lakhs: "))
    
    # Convert salary to actual amount
    salary_amount = a * 100000
    
    # Calculate the deductions
    hra = salary_amount * 0.10  # 10% HRA
    da = salary_amount * 0.05   # 5% DA
    pf = salary_amount * 0.03   # 3% PF
    
    # Initialize tax variable
    tax = 0
    
    # Calculate the tax based on salary range
    if 5 <= a <= 10:
        tax = salary_amount * 0.10  # 10% tax
    elif 11 <= a <= 20:
        tax = salary_amount * 0.20  # 20% tax
    elif a > 20:
        tax = salary_amount * 0.30  # 30% tax
    elif a <= 1:
        print("k")
        return  # Exit the function early if salary is between 0-1 lakh
    
    # Calculate in-hand salary
    inhand = salary_amount - (hra + da + pf + tax)
    
    # Print the in-hand salary
    print("Your in-hand salary is ₹", inhand)

salary()
