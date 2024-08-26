two_d_list = [
    list(map(int, input("Enter the first row items separated by spaces: ").split())),
    list(map(int, input("Enter the second row items separated by spaces: ").split()))
    # Add more rows if needed
]

one_d_list = [item for sublist in two_d_list for item in sublist]

print("The 1D list is:", one_d_list)
