import numpy as np
import matplotlib.pyplot as plt

# Define the discrete time range for Signal 1
k1 = np.arange(-10, 21)

# Signal 1: f[k] = -0.92 sin(0.1 pi k - 3 pi / 4)
f1 = -0.92 * np.sin(0.1 * np.pi * k1 - 3 * np.pi / 4)

# Plot Signal 1
plt.figure(figsize=(10, 4))
plt.stem(k1, f1, basefmt=" ")
plt.title(r'Signal 1: $f[k] = -0.92 \sin(0.1 \pi k - \frac{3 \pi}{4})$')
plt.xlabel('k')
plt.ylabel('$f[k]$')
plt.grid(True)
plt.show()

# Define the discrete time range for Signal 2
k2 = np.arange(0, 51)

# Signal 2: f[k] = (-0.93)^k * e^(j pi k / sqrt(350))
f2 = (-0.93)**k2 * np.exp(1j * np.pi * k2 / np.sqrt(350))

# Plot the magnitude of Signal 2
plt.figure(figsize=(10, 4))
plt.stem(k2, np.abs(f2), basefmt=" ")
plt.title(r'Signal 2: $f[k] = (-0.93)^k \cdot e^{j \pi k / \sqrt{350}}$ (Magnitude)')
plt.xlabel('k')
plt.ylabel('$|f[k]|$')
plt.grid(True)
plt.show()

# # Plot the phase of Signal 2
# plt.figure(figsize=(10, 4))
# plt.stem(k2, np.angle(f2), basefmt=" ")
# plt.title(r'Signal 2: $f[k] = (-0.93)^k \cdot e^{j \pi k / \sqrt{350}}$ (Phase)')
# plt.xlabel('k')
# plt.ylabel('Phase of $f[k]$')
# plt.grid(True)
# plt.show()
