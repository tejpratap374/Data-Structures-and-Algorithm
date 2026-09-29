# Rotate a square matrix by 90 degrees clockwise.
def rotate(matrix):
    n = len(matrix)

    # Step 1: transpose the matrix (swap elements across the main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row to complete the clockwise rotation
    for i in range(n):
        matrix[i].reverse()

    return matrix


# Print matrix rows in a readable format.
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()


# Example matrix.
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

print("Original Matrix:")
printMatrix(matrix)
print()

rotate(matrix)
print("Rotated Matrix (90° clockwise):")
printMatrix(matrix)
