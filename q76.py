rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
matrix1 = [list(map(int, input(f"Enter row {i+1} of the first matrix separated by spaces: ").split())) for i in range(rows1)]

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
matrix2 = [list(map(int, input(f"Enter row {i+1} of the second matrix separated by spaces: ").split())) for i in range(rows2)]

if cols1 != rows2:
    print("Matrix multiplication cannot be performed.")
else:
    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    print("The result of matrix multiplication is:")
    for row in result:
        print(' '.join(map(str, row)))
