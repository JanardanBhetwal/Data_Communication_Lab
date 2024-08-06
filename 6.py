import numpy as np

# Define the range for k
k = np.arange(1, 31)

# Calculate the function values
f = np.exp(0.05 * k)

# a) Calculate the maximum value in f
max_value = np.max(f)
print(f"Maximum value: {max_value}")

# b) Calculate the minimum value in f
min_value = np.min(f)
print(f"Minimum value: {min_value}")

# c) Sum all the entries in f
sum_value = np.sum(f)
print(f"Sum of all entries: {sum_value}")

# d) Find the product of all the entries in f
product_value = np.prod(f)
print(f"Product of all entries: {product_value}")

# e) Find the mean of all the entries in f
mean_value = np.mean(f)
print(f"Mean of all entries: {mean_value}")

# f) Find the variance of all the entries in f
variance_value = np.var(f)
print(f"Variance of all entries: {variance_value}")

# g) Find the dimension of f (number of dimensions)
dimension_value = f.ndim
print(f"Dimension of f: {dimension_value}")

# h) Find the length of f (number of elements)
length_value = len(f)
print(f"Length of f: {length_value}")


import numpy as np

# Define the matrices X and Y
X = np.array([[2, 5], [4, 6]])
Y = np.array([[1, 5], [6, -2]])

# a) Find the sum of X and Y
sum_XY = X + Y
print("Sum of X and Y:\n", sum_XY)

# b) Find the difference between X and Y
diff_XY = X - Y
print("\nDifference between X and Y:\n", diff_XY)

# c) Find the product between X and Y (matrix multiplication)
product_XY = np.dot(X, Y)
print("\nProduct of X and Y (matrix multiplication):\n", product_XY)

# d) Calculate the transpose of X
transpose_X = np.transpose(X)
print("\nTranspose of X:\n", transpose_X)

# e) Calculate the inverse of X
inverse_X = np.linalg.inv(X)
print("\nInverse of X:\n", inverse_X)

# f) Perform an element-by-element multiplication between X and Y
elementwise_mult_XY = np.multiply(X, Y)
print("\nElement-by-element multiplication between X and Y:\n", elementwise_mult_XY)

# g) Perform an element-by-element division between X and Y
elementwise_div_XY = np.divide(X, Y)
print("\nElement-by-element division between X and Y:\n", elementwise_div_XY)

# h) Square each element of X
squared_X = np.square(X)
print("\nSquare of each element in X:\n", squared_X)

# i) Raise each element in X to the power of its corresponding element in Y
power_XY = np.power(X.astype(float), Y.astype(float))
np.set_printoptions(precision=2, suppress=True)
print("\nElement in X raised to the power of its corresponding element in Y:\n", power_XY)


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
