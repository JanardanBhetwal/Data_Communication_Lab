# Equivalent Python Code Using for Loop
# Initializing the matrices
x = [[2, 5], [4, 6]]
y = [[1, 5], [6, -2]]
z = [[0, 0], [0, 0]]

# Using for loop to add matrices x and y
for m in range(2):
    for n in range(2):
        z[m][n] = x[m][n] + y[m][n]

# Printing the result
for row in z:
    print(row)


# Equivalent Python Code Using while Loop
# Initializing the matrices
x = [[2, 5], [4, 6]]
y = [[1, 5], [6, -2]]
z = [[0, 0], [0, 0]]

# Using while loop to add matrices x and y
m = 0
while m < 2:
    n = 0
    while n < 2:
        z[m][n] = x[m][n] + y[m][n]
        n += 1
    m += 1

# Printing the result
for row in z:
    print(row)


# Python Code Without Using Loops (Direct Sum of Matrices)
import numpy as np

# Initializing the matrices
x = np.array([[2, 5], [4, 6]])
y = np.array([[1, 5], [6, -2]])

# Performing direct sum of matrices x and y
z = x + y

# Printing the result
print(z)
