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
