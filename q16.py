def weather():
    t = int(input("Enter the temperature : "))
    h = int(input("Enter the humidity : "))
    if(t>=30 and h>=90):
        print(f"The waether at temperature {t} and humidity {h} is HOT AND HUMID ")
    elif(t>=30 and h<90):
        print(f"The waether at temperature {t} and humidity {h} is HOT")
    elif(t<30 and h>=90):
        print(f"The waether at temperature {t} and humidity {h} is COOL AND HUMID")
    elif(t<30 and h<90):
        print(f"The waether at temperature {t} and humidity {h} is COOL AND HUMID ")
    else:
        print("Invalid input")
weather()