# Generates the frequency table and histogram of a set of numbers
# Frequency table gets printed to console while the histogram appears on a new window

# Usage: $python frequencies.py <input file name> <expected number of decimals>

# Student: Adolfo Acosta Castro [A01705249]
# Date: 25/august/2022
# Class: Metodos cuantitativos y simulacion

import sys
import math
import matplotlib.pyplot as plt

LOWER_LIM = 0
UPPER_LIM = 1

'''
Truncates decimals after a given ammount of decimal digits
'''
def truncate(value, decimalsToKeep):
    return math.trunc(value * 10**decimalsToKeep) / (10**decimalsToKeep)

'''
Returns the number of classes according to Sturge's rule given a dataset size
'''
def sturgesClassNumber(n):
    return 1 + math.ceil(3.3 * math.log10(n))

# Get arguments from console
fileName = sys.argv[1]
decimalPlaces = int(sys.argv[2])

# Read values from file
file = open(fileName, 'r')
values = file.readlines()
n = len(values)

# Clean up and truncate values
for i in range(n):
    values[i] = truncate(float(values[i].strip()), decimalPlaces)

# Calculate number of intervals
classes = sturgesClassNumber(n)

# Find largest and smallest value
minValue = min(values)
maxValue = max(values)

# Calculate interval width
width = (maxValue - minValue) / classes
width = truncate(width, decimalPlaces) + (1 / 10**decimalPlaces)

# Store interval limits
limits = [[0] * 2 for i in range(classes)] # where's the fridge python

limits[0][LOWER_LIM] = minValue
limits[0][UPPER_LIM] = minValue + width

for i in range(classes):
    if i == 0:
        continue
    limits[i][LOWER_LIM] = limits[i-1][UPPER_LIM]
    limits[i][UPPER_LIM] = limits[i][LOWER_LIM] + width

# Count frequencies
frequencies = [0] * classes
frequenciesSum = 0
for i in range(n):
    # Note: the asymptotic complexity can be reduced from O(n*classes) to
    # O(n*log2(classes)) by replacing this loop with binary search. It'd
    # be worth considering for enormous datasets
    for j in range(classes):
        if limits[j][LOWER_LIM] <= values[i] and values[i] < limits[j][UPPER_LIM]:
            frequencies[j] += 1
            frequenciesSum += 1
            break

# Print calculated values and frequencies
print(f"N: {n}")
print(f"C: {classes}")
print(f"Max: {maxValue:.{decimalPlaces}f}, min: {minValue:.{decimalPlaces}f}")
print(f"Width: {width:.{decimalPlaces}f}\n")

print("Intervals              f")
for i in range(classes):
    print(f"[{limits[i][LOWER_LIM]:.{decimalPlaces}f},", end="")
    print(f" {limits[i][UPPER_LIM]:.{decimalPlaces}f})", end="")
    print(f"      {frequencies[i]}")

print(f"\nSum of frequencies: {frequenciesSum}")

# Show histogram
bar_labels = list(range(classes))
plt.bar(bar_labels, frequencies, tick_label = bar_labels, color = ['teal'])
plt.xlabel('Classes')
plt.ylabel('Frequencies')
plt.title('Frequencies histogram')
plt.show()