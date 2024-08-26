rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
matrix1 = [list(map(int, input(f"Enter row {i+1} of the first matrix separated by spaces: ").split())) for i in range(rows1)]

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
matrix2 = [list(map(int, input(f"Enter row {i+1} of the second matrix separated by spaces: ").split())) for i in range(rows2)]

if cols1 == rows2:
    print("Matrix multiplication can be performed.")
else:
    print("Matrix multiplication cannot be performed.")
