rows_a=int(input("enter the number of rows for the first matrix:"))
column_a=int(input("Enter the number of columns for the first matrix:"))
print("Enter the elements of first matrix:")
matrix_a=[[int(input())for i in range(column_a)]for i in range(rows_a)]
print("First matrix is:")
for n in matrix_a:
    print(n)
    column_b=int(input("Enter the number of columns for the second matrix:"))
print("Enter the elements of second matrix:")
matrix_b=[[int(input())for i in range(column_b)]
    for i in range(column_a)]
print("Second matrix is:")
for n in matrix_b:
    print(n)
result=[[0 for i in range(column_b)]
for i in range(rows_a)]
for i in range(len(matrix_a)):
    for j in range(len(matrix_b)):
        for R in range(len(matrix_b)):
            result[i][j]+=matrix_a[i][R]*matrix_b[R][j]
print("Multiplication of two matrices:")
print("In matrix_a X Matrix_b is:")
for r in result:
    print(r)
                
    
