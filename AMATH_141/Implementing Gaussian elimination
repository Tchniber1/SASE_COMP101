import numpy as np
def solve_system(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError as e:
        print("Error:", e)
        return None
A = np.array([[3, 2], [1, 4]])
b = np.array([[5], [6]])   
x = solve_system(A, b)
print("Solution x:\n", x)
def gaussian_elimination(A, b):
    """Solve A x = b using Gaussian elimination without pivoting.

    Parameters
    ----------
    A : np.ndarray of shape (n, n)
        Coefficient matrix.
    b : np.ndarray of shape (n, 1)
        Right-hand side column vector.
    """
    # TODO: implement forward elimination and back-substitution
    # and return x as an (n, 1) array.
    n = len(A)
    augmented = np.hstack((A, b)).astype(float)
    for i in range(n):
        for j in range(i + 1, n):
            factor = augmented[j, i] / augmented[i, i]
            augmented[j] = augmented[j] - factor * augmented[i]
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):  
        x[i] = (augmented[i, -1] - np.dot(augmented[i, i + 1:n], x[i + 1:n].flatten())) / augmented[i, i]
    return x
x_gaussian = gaussian_elimination(A, b)
print("Solution x from Gaussian elimination:\n", x_gaussian)
comparison = np.allclose(x, x_gaussian,)
print("Are the solutions from solve_system and Gaussian elimination close?", comparison)


    

