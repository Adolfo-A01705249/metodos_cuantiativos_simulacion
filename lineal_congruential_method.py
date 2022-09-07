# Generates 10 numbers with preset parameters using
# Linear Congruential method.

# Usage: $python lineal_congruential_method.py

# Author: Guillermo C. Espino [A01704354]
# Date: 30/august/2022
# Class: Metodos cuantitativos y simulacion

print("Linear Congruential Method\n")

# Inputs
Xo = int(input("Enter the value of Xo: ")) #6
a = int(input("Enter the value of a: ")) #32
c = int(input("Enter the value of c: ")) #3
m = int(input("Enter the value of m: ")) #80

Xi = Xo

res = 0

lcfile = open('random_numers_lcm.txt', 'w')
print("\nThe numbers are:")
for x in range(10):
    Xi = ((a * Xi) + c) % m
    res = float(Xi / m)
    print(res)
    print(res, file = lcfile)
    
lcfile.close()