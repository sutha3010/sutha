rows=int(input("Enter the number of rows:"))
column=int(input("Enter the number of columns:"))
print("Enter the elements of matrix:")
matrix=[[int(input())for i in range(column)]for i in range(rows)]
print("Matrix is:")
for n in matrix:
    print(n)
    result=[[0 for i in range(rows)]for j in range(column)]
for r in range(rows):
    for c in range(column):
           result[c][r]=matrix[r][c]
print("Transpose Matrix:")
for r in result:
    print(r)
