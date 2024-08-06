import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 5
t = np.linspace(-L, L, 1000)

# Define the function
g_t = -t**4 + 17*t**3 - t**2 - 47

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(t, g_t, label='$g(t) = -t^4 + 17t^3 - t^2 - 47$')
plt.title('Function $g(t)$')
plt.xlabel('Time (s)')
plt.ylabel('$g(t)$')
plt.grid(True)
plt.legend()
plt.show()


from scipy.integrate import quad

# Define the function to compute Fourier coefficients
def compute_fourier_coefficients(n, L):
    def integrand(t, n):
        return (-t**4 + 17*t**3 - t**2 - 47) * np.cos(n * np.pi * t / L)
    a_n, _ = quad(integrand, -L, L, args=(n))
    return (2 / L) * a_n

# Fourier series approximation
def fourier_series_approximation(t, m, L):
    result = np.zeros_like(t)
    for n in range(1, m + 1):
        a_n = compute_fourier_coefficients(n, L)
        result += a_n * np.cos(n * np.pi * t / L)
    return result

# Number of terms in Fourier series
terms_list = [1, 5, 10, 20]

# Plot the Fourier series approximations
plt.figure(figsize=(14, 10))
for m in terms_list:
    g_approx = fourier_series_approximation(t, m, L)
    plt.plot(t, g_approx, label=f'Fourier Series (m = {m})')

plt.title('Fourier Series Approximation of $g(t)$')
plt.xlabel('Time (s)')
plt.ylabel('$g(t)$')
plt.grid(True)
plt.legend()
plt.show()
