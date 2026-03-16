import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        A = np.asarray(matrix)
    except ValueError:
        return None

    if A.ndim != 2 or A.size == 0 or A.shape[0] != A.shape[1]:
        return None

    eigen_vals = np.linalg.eigvals(A)  

    idx = np.lexsort((eigen_vals.imag, eigen_vals.real))

    return eigen_vals[idx]