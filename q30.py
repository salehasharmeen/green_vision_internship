def calculate_population():
    current_population = 10000
    rate_of_increase = 0.10
    
    for year in range(10, 0, -1):
        print(f"{year}th year - {int(current_population)}")
        current_population /= (1 + rate_of_increase)

calculate_population()
