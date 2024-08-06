import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 10000  # Sampling frequency
T = 1       # Duration of the signal in seconds
f_c1 = 10  # Frequency of the carrier signal for binary 0
f_c2 = 100  # Frequency of the carrier signal for binary 1
f_m = 2     # Frequency of the message signal in Hz
A_c = 1     # Amplitude of the carrier signal

# Time vector
t = np.arange(0, T, 1/Fs)

# Digital Message Signal
# Create a binary signal with period T / f_m
message_signal = np.sign(np.sin(2 * np.pi * f_m * t))  # Binary signal: -1 and 1

# FSK Signal
# Use f_c1 for binary 0 and f_c2 for binary 1
fsk_signal = np.where(message_signal > 0, 
                      A_c * np.sin(2 * np.pi * f_c2 * t), 
                      A_c * np.sin(2 * np.pi * f_c1 * t))

# Plot Digital Message Signal
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message_signal, label='Message Signal', color='blue')
plt.title('Digital Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot Carrier Signals
carrier_signal_0 = A_c * np.sin(2 * np.pi * f_c1 * t)
carrier_signal_1 = A_c * np.sin(2 * np.pi * f_c2 * t)

plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal_0, label='Carrier Signal for Binary 0', color='red', linestyle='--')
plt.plot(t, carrier_signal_1, label='Carrier Signal for Binary 1', color='green', linestyle='--')
plt.title('Carrier Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot FSK Signal
plt.subplot(3, 1, 3)
plt.plot(t, fsk_signal, label='FSK Signal', color='orange')
plt.title('Frequency Shift Keyed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
