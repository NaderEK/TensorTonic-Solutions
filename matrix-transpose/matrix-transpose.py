import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows, cols = len(A), len(A[0])

    new_matrix = [[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = A[i][j] 
    return np.asarray(new_matrix)
