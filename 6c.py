
import numpy as np

# Define the vectors f and g
f = np.array([1, 4, -2, 4-2j])
g = np.array([-3, 5+7j, 6, 2])

# a) Addition r1
r1 = f + g
print("Addition (r1):", r1)

# b) Dot product r2
r2 = np.dot(f, g)
print("\nDot product (r2):", r2)

# c) Mean r3
r3 = np.mean(f)
print("\nMean (r3):", r3)

# d) Average energy r4
r4 = np.sum(np.abs(f)**2) / len(f)
print("\nAverage energy (r4):", r4)
