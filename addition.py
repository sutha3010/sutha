rows=int(input("enter the number of rows:"))
column=int(input("Enter the number of columns:"))
print("Enter the elements of first matrix:")
matrix_a=[[int(input())for i in range(column)]for i in range(rows)]
print("First matrix is:")
for n in matrix_a:
    print(n)
print("Enter the elements of second matrix:")
matrix_b=[[int(input())for i in range(column)]for i in range(rows)]
for n in matrix_b:
    print(n)
result=[[0 for i in range(column)]for i in range(rows)]
for i in range(rows):
    for j in range(column):
        result[i][j]=matrix_a[i][j]+matrix_b[i][j]
print("The Sum of above two matrices is:")
for r in result:
 print(r)
                
