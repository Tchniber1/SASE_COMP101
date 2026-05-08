import numpy as np

def jacobi(A, b, x0=None, tol=1e-8, max_iter=10000):
    A = np.asarray(A, dtype=float)
    b_in = np.asarray(b, dtype=float)
    b = b_in.ravel()
    n = A.shape[0]

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.asarray(x0, dtype=float).ravel().copy()

    D = np.diag(A)
    R = A - np.diag(D)
    b_norm = np.linalg.norm(b)
    if b_norm == 0.0:
        b_norm = 1.0

    iters = 0
    for k in range(1, max_iter + 1):
        x_new = (b - R @ x) / D
        iters = k
        if np.linalg.norm(A @ x_new - b) / b_norm <= tol:
            x = x_new
            break
        x = x_new
    if b_in.ndim == 2:
        x = x.reshape(-1, 1)
    return x, iters