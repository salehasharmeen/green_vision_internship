def getangle():
    h =int(input("Enter the hour hand time : "))
    m=int(input("Enter the minute hand time : "))
    minute_angle = 6 * m
    hour_angle = 30 * h + 0.5 * m
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    
    return angle

angle = getangle()
print(f"The angle between the hour and minute hand is {angle} degrees.")

