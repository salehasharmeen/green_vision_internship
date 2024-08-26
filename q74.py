rows = int(input("Enter the number of rows: "))
matrix = [list(map(int, input(f"Enter row {i+1} items separated by spaces: ").split())) for i in range(rows)]

num_rows = len(matrix)
num_cols = len(matrix[0]) if num_rows > 0 else 0

print(f"The shape of the matrix is: {num_rows} x {num_cols}")
