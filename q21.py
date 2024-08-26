def cm_to_ft():
    c = int(input("Enter your length in cm: "))
    f = c / 30.48
    print(f"{c} cm in ft is {f:.2f}")

def km_to_mile():
    k = int(input("Enter your distance in km: "))
    m = k * 0.621371
    print(f"{k} km in miles is {m:.2f}")

def usd_to_pkr():
    u = float(input("Enter your currency in USD: "))
    p = u * 300  # Assuming the exchange rate is 300 PKR per USD
    print(f"{u:.2f} USD in PKR is {p:.2f}")

def main():
    print("\nChoose what you want for conversion:")
    print("1. cm to ft")
    print("2. km to miles")
    print("3. USD to PKR")
    print("4. Exit")
        
    choice = int(input("Enter your choice (1-4): "))
        
    if choice == 1:
        cm_to_ft()
    elif choice == 2:
        km_to_mile()
    elif choice == 3:
        usd_to_pkr()
    elif choice == 4:
        print("Exiting the program. Goodbye!")
            
    else:
        print("Invalid choice, please select a valid option.")

# Run the program
main()
