import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 10000  # Sampling frequency (high resolution)
T = 1       # Duration of the signal in seconds
f_c = 100  # Frequency of the carrier signal in Hz (high frequency for clear phase shift)
f_m = 5     # Frequency of the message signal in Hz (lower frequency)
A_c = 1     # Amplitude of the carrier signal

# Time vector
t = np.arange(0, T, 1/Fs)

# Digital Message Signal
# Create a binary signal with period T / f_m
message_signal = np.sign(np.sin(2 * np.pi * f_m * t))  # Binary signal: -1 and 1

# PSK Signal
# 0 -> phase shift of 0 radians, 1 -> phase shift of π radians
# Map -1 to 0 radians and 1 to π radians
phase_shift = np.where(message_signal > 0, 0, np.pi)
psk_signal = A_c * np.sin(2 * np.pi * f_c * t + phase_shift)

# Plot Digital Message Signal
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message_signal, label='Message Signal', color='blue')
plt.title('Digital Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Carrier Signal
carrier_signal = A_c * np.sin(2 * np.pi * f_c * t)
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal, label='Carrier Signal', color='orange')
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot PSK Signal
plt.subplot(3, 1, 3)
plt.plot(t, psk_signal, label='PSK Signal', color='green')
plt.title('Phase Shift Keyed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
