import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000  # Sampling frequency
T = 1       # Duration of the signal in seconds
f_c = 100   # Frequency of the carrier signal in Hz
f_m = 2     # Frequency of the message signal in Hz
A_c_high = 1   # Amplitude of the carrier signal when message is 1
A_c_low = 0.2  # Amplitude of the carrier signal when message is 0
A_m = 1     # Amplitude of the message signal (used to determine levels)

# Time vector
t = np.arange(0, T, 1/Fs)

# Digital Message Signal
# Create a binary signal with period T / f_m
message_signal = np.sign(np.sin(2 * np.pi * f_m * t))  # Binary signal: -1 and 1

# Carrier Signal
carrier_signal = np.sin(2 * np.pi * f_c * t)

# ASK Signal
# Scale the carrier signal based on the message signal
ask_signal = np.where(message_signal > 0, A_c_high * carrier_signal, A_c_low * carrier_signal)

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
plt.plot(t, A_c_high * carrier_signal, label='Carrier Signal', color='orange')
plt.title('Carrier Signal (High Amplitude)')
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
