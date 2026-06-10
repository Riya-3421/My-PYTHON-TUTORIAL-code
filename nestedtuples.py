##create a nested tuple representing  3*3 matrix and print the matrix.Access and print the element at the second row and third column

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("Matrix:")
for row in matrix:
    print(row)
print(f"Element at second row and third column: {matrix[1][2]}")