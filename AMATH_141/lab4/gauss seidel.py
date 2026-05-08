import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-8, max_iter=10000):
    A = np.asarray(A, dtype=float)
    b_in = np.asarray(b, dtype=float)
    b = b_in.ravel()
    n = A.shape[0]

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.asarray(x0, dtype=float).ravel().copy()

    b_norm = np.linalg.norm(b)
    if b_norm == 0.0:
        b_norm = 1.0

    iters = 0
    for k in range(1, max_iter + 1):
        for i in range(n):
            s1 = A[i, :i] @ x[:i]        
            s2 = A[i, i+1:] @ x[i+1:]  
            x[i] = (b[i] - s1 - s2) / A[i, i]
        iters = k
        if np.linalg.norm(A @ x - b) / b_norm <= tol:
            break

    if b_in.ndim == 2:
        x = x.reshape(-1, 1)
    return x, iters