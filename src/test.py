#!/usr/bin/env python

# https://www.youtube.com/watch?v=4TdITPIn0ww

from fft import fft
import numpy as np
import matplotlib.pyplot as plt

g = lambda x: x**4 - 3 * x**3 + 2 * x**2 - np.tan(x * (x - 2))

a = 0
b = 2

z = lambda x: a + x * (b - a) / (2 * np.pi)
f = lambda x: g(z(x))

m = 2

C = fft(f, m)
print(C)

N = 2**m
A = 2 * C[0 : N // 2].real
A[0] = 0.5 * A[0]
print(f"A = {A}")

B = -2 * C[0 : N // 2].imag
print(f"B = {B}")

xx = np.linspace(0, 2 * np.pi, 200)
yy = sum(
    [(A[k] * np.cos(k * xx) + B[k] * np.sin(k * xx))[:, None] for k in range(len(A))]
)
tt = np.linspace(0, 2 * np.pi * (N - 1.0) / N, N)

plt.plot(z(xx), yy, "r", linewidth=0.3)
plt.plot(z(xx), g(z(xx)), "g", linewidth=0.3)
plt.plot(z(tt), f(tt), 'o', 'c')
plt.savefig("figura.pdf")
