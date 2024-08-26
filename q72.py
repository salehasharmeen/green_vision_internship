rows = int(input("Enter the number of rows: "))
matrix = [list(map(int, input(f"Enter row {i+1} items separated by spaces: ").split())) for i in range(rows)]

max_in_rows = [max(row) for row in matrix]

print("Max item of each row:", max_in_rows)
