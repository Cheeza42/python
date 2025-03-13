def get_matrix(rows, cols):

    matrix = []
    print(f"Enter the elements of a {rows}x{cols} matrix row by row: ")
    for i in range(rows):  
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return matrix
def multiply_matrices(A, B):

    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication is not possible!")
        return None
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def print_matrix(matrix):
    
    for row in matrix:
    
     print(" ".join(map(str, row)))

rows_A = int(input("Please enter number of rows for matrix A: "))
cols_A = int(input("Please enter a number of columns for matrix A:  "))

rows_B = int(input("Please enter number of rows for matrix B: "))
cols_B = int(input("Please enter a number of columns for matrix B:  "))

A = get_matrix(rows_A, cols_A)
B = get_matrix(rows_B, cols_B)

result = multiply_matrices(A, B)
if result:
    print("Resulting matrix:")
    print_matrix(result)
