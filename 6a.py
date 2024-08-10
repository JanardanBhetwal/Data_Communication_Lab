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