import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 10000  # Sampling frequency
t = np.arange(0, 1, 1/Fs)  # Time vector
f_m = 5  # Frequency of message signal
f_c = 100  # Frequency of carrier signal
A_m = 2  # Amplitude of message signal
A_c = 1  # Amplitude of carrier signal

# Message and carrier signals
message_signal = A_m * np.sin(2 * np.pi * f_m * t)
carrier_signal = A_c * np.sin(2 * np.pi * f_c * t)

# AM signal
am_signal = (A_c + message_signal) * np.sin(2 * np.pi * f_c * t)

# Plot AM signal
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, message_signal)
plt.title('Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title('Amplitude Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
