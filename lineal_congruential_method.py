# Generates 10 numbers with preset parameters using
# Linear Congruential method.

# Usage: $python lineal_congruential_method.py

# Author: Guillermo C. Espino [A01704354]
# Date: 30/august/2022
# Class: Metodos cuantitativos y simulacion

Xo = 6
a = 32
c = 3
m = 80
Xi = Xo

res = 0

for x in range(10):
    Xi = ((a * Xi) + c) % m
    res = float(Xi / m)
    print(res)