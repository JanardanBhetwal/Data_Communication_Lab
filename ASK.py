import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000  # Sampling frequency
T = 1       # Duration of the signal in seconds
f_c = 100  # Frequency of the carrier signal in Hz
f_m = 2     # Frequency of the message signal in Hz
A_c = 1     # Amplitude of the carrier signal
A_m = 1     # Amplitude of the message signal

# Time vector
t = np.arange(0, T, 1/Fs)

# Digital Message Signal
# Create a binary signal with period T / f_m
message_signal = A_m * np.sign(np.sin(2 * np.pi * f_m * t))

# Carrier Signal
carrier_signal = A_c * np.sin(2 * np.pi * f_c * t)

# ASK Signal
# Modulate the carrier signal using the message signal
ask_signal = (A_m * (message_signal + 1)) * np.sin(2 * np.pi * f_c * t)

# Plot Digital Message Signal
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message_signal, label='Message Signal')
plt.title('Digital Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal, label='Carrier Signal', color='orange')
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot ASK Signal
plt.subplot(3, 1, 3)
plt.plot(t, ask_signal, label='ASK Signal', color='green')
plt.title('Amplitude Shift Keyed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
