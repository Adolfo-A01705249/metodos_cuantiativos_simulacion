# Tests whether a sequence of numbers in [0, 1] is random
# by using the runs test

# Usage: $python runs_test.py <input file name>

# Author: Valeria Guerra de la O [A01705318]
# Date: 31/august/2022
# Class: Metodos cuantitativos y simulacion

import sys
import math

CRITICAL_ZET = 1.96

# Get arguments from console
fileName = sys.argv[1]

# Read values from file 
file = open(fileName,'r')
contents = file.readlines()
n = len(contents)

# Get signs
rachas = list()
before = contents[0]
for i in range(n):
    if i != 0:
        if contents[i] >= before:
            rachas.append('+')
        else:
            rachas.append('-')
        before = contents[i]

# Get total signs
n_signos = len(rachas)

# Get total runs
t_runs = 1
for i in range(n_signos-1):
    if rachas[i] != rachas[i+1]:
        t_runs = t_runs + 1
        
# Get Mui
mui = ((2 * n_signos) - 1) / 3

# Get sigma
sigma2 = ((16 * n_signos) - 29) / 90
sigma = math.sqrt(sigma2)

# Get zscore (numero de rachaz - mui / sigma)
zscore = (t_runs - mui) / sigma

# Print calculated values and conclusion
print('Generated signs:')
SIGNS_LIMIT = 100
if n_signos > SIGNS_LIMIT:
    print_signs = input(f'There\'s a large number of signs ({n_signos}), would you like to see them anyway? (Y/N): ')
    if print_signs == 'Y':
        print(*rachas)
    else:
        print('---Signs skipped')
else:
    print(*rachas)
        
print(f'total signs: {n_signos}')
print(f'total runs: {t_runs}')

print('\nStatistics')
print(f'Mui = {mui:.6f}')
print(f'Sigma = {sigma:.6f}')
print(f'Zscore = {zscore:.6f}')

print('\nH0: Appereance of the numbers is random')
print('H1: Appereance of the numbers is not random')

# |zscore| > Za/2 (is rejected)
if(abs(zscore) >= CRITICAL_ZET):
    print(f'Since |{zscore:.6f}| >= |{CRITICAL_ZET}| H0 is rejected')
else:
    print(f'Since |{zscore:.6f}| < |{CRITICAL_ZET}| H0 is not rejected')