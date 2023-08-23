import numpy as np


def fft(f, m):
    N = 2**m
    print(f"N = {N}")
    w = np.exp(-2 * np.pi * 1j / N)
    C = np.zeros((N,), dtype=complex)
    xx = np.linspace(0, 2 * np.pi * (N - 1) / N, N)
    C[:] = f(xx)
    D = np.zeros_like(C)
    Z = np.array([w**k for k in range(N)])

    for n in range(m):
        for k in range(2 ** (m - n - 1)):
            for j in range(2 ** (n)):
                u = C[2**n * k + j]
                v = Z[j * 2 ** (m - n - 1)] * C[2**n * k + 2 ** (m - 1) + j]
                D[2 ** (n + 1) * k + j] = (u + v) / 2
                D[2 ** (n + 1) * k + j + 2**n] = (u - v) / 2
        C[:] = D[:]
    return C
