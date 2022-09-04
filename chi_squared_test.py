# Tests whether a sequence of random numbers in [0, 1] is uniformly
# distrutted by running the chi squared test

# Usage: $python chi_squared_test.py <input file name>

# Author: Adolfo Acosta Castro [A01705249]
# Date: 30/august/2022
# Class: Metodos cuantitativos y simulacion

import sys

CRITICAL_VAL = 16.919 # For our fixed df = 10 - 1 and alpha = 0.05
INTERVAL_N = 10
INTERVAL_WIDTH = 0.1

# Get arguments from console
fileName = sys.argv[1]

# Read values from file
file = open(fileName, 'r')
values = file.readlines()
n = len(values)

# Clean up and prepare values
for i in range(n):
    values[i] = float(values[i].strip())

# Store interval limits
lower_lim = [0] * INTERVAL_N
upper_lim = [0] * INTERVAL_N
for i in range(INTERVAL_N):
    lower_lim[i] = i * 0.1
    upper_lim[i] = lower_lim[i] + INTERVAL_WIDTH

# Count frequencies
frequencies = [0] * INTERVAL_N
frequenciesSum = 0
for i in range(n):
    for j in range(INTERVAL_N):
        # Only the second part of the condition is necessary but
        # writing it like this makes it more readable
        if lower_lim[j] <= values[i] and values[i] < upper_lim[j]:
            frequencies[j] += 1
            frequenciesSum += 1
            break

if(frequenciesSum != n):
    sys.exit("Error: some values were not counted.")

# Calculate differences between expected and actual frequencies
expected_freq = n / INTERVAL_N
test_stats = [0] * INTERVAL_N
chi = 0
for i in range(INTERVAL_N):
    test_stats[i] = (frequencies[i] - expected_freq)**2 / expected_freq
    chi += test_stats[i]

# Print frequencies, calculated values, and conclusion
print("Intervals              Observed        Expected           (O - E)^2 / E")
for i in range(INTERVAL_N):
    print(f"[{lower_lim[i]:.1f} - {upper_lim[i]:.1f})              ", end="")
    print(f"{frequencies[i]}              ", end="")
    print(f"{expected_freq:.4f}                ", end="")
    print(f"{test_stats[i]:.4f}")

print(f"\nX^2 = {chi:.4f}")

print("\nH0: Generated numbers are not different from the uniform distribution")
print("H1: Generated numbers are different from the uniform distribution\n")

if(chi >= CRITICAL_VAL):
    print(f"Since {chi:.4f} >= {CRITICAL_VAL}, H0 is rejected")
else:
    print(f"Since {chi:.4f} < {CRITICAL_VAL}, H0 is not rejected")