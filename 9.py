import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 1  # Hz
amplitude = 5  # Volts
dc_bias = -3   # Volts
time_interval = (-3, 3)  # seconds

# Time vector
t = np.linspace(time_interval[0], time_interval[1], 1000)

# Generate the square wave
g_t = amplitude * np.sign(np.sin(2 * np.pi * frequency * t)) + dc_bias

# Plot the square wave
plt.figure(figsize=(10, 6))
plt.plot(t, g_t, label='Square Wave')
plt.title('Square Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.show()
# Fourier series approximation
def fourier_series_approximation(t, n_terms):
    result = np.zeros_like(t)
    for n in range(1, n_terms + 1, 2):  # Only odd harmonics
        result += (4 * amplitude / (np.pi * n)) * np.sin(2 * np.pi * n * frequency * t)
    return result + dc_bias

# Number of terms in Fourier series
terms_list = [1, 5, 10, 20]

# Plot the Fourier series approximations
plt.figure(figsize=(14, 10))
for m in terms_list:
    g_approx = fourier_series_approximation(t, m)
    plt.plot(t, g_approx, label=f'Fourier Series (m = {m})')

plt.title('Fourier Series Approximation of Square Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.show()
