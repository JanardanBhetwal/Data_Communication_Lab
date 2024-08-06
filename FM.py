import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 10000  # Sampling frequency
t = np.arange(0, 1, 1/Fs)  # Time vector from 0 to 1 second
f_m = 5  # Frequency of message signal in Hz
f_c = 100  # Frequency of carrier signal in Hz
A_m = 1  # Amplitude of message signal
beta = 15  # Modulation index (frequency deviation)

# Message signal
message_signal = A_m * np.sin(2 * np.pi * f_m * t)

# Carrier signal
carrier_signal = np.sin(2 * np.pi * f_c * t)

# FM signal
# The phase of the carrier is modulated by the message signal
fm_signal = np.sin(2 * np.pi * f_c * t + beta * np.sin(2 * np.pi * f_m * t))

# Plot Message Signal
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message_signal)
plt.title('Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot FM Signal
plt.subplot(3, 1, 3)
plt.plot(t, fm_signal)
plt.title('Frequency Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
