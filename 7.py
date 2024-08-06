import numpy as np
import matplotlib.pyplot as plt

# Define the time range for the first signal
t1 = np.linspace(-5, 5, 1000)

# Define the first signal
x1 = 5 * np.sin(2 * np.pi * t1) * np.cos(np.pi * t1 - 8)

# Plot the first signal
plt.figure(figsize=(10, 4))
plt.plot(t1, x1)
plt.title('Signal 1: $x(t) = 5 \sin(2\pi t) \cos(\pi t - 8)$')
plt.xlabel('Time (t)')
plt.ylabel('$x(t)$')
plt.grid(True)
plt.show()

# Define the time range for the second signal
t2 = np.linspace(-10, 10, 1000)

# Define the second signal
x2 = 5 * np.exp(-0.2 * t2) * np.sin(2 * np.pi * t2)

# Plot the second signal
plt.figure(figsize=(10, 4))
plt.plot(t2, x2)
plt.title('Signal 2: $x(t) = 5 e^{-0.2t} \sin(2 \pi t)$')
plt.xlabel('Time (t)')
plt.ylabel('$x(t)$')
plt.grid(True)
plt.show()
