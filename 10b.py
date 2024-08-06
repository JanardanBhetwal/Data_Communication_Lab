import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 5  # Hz
amplitude = 19  # Volts
time_interval = (0, 3)  # seconds

# Time vector
t = np.linspace(time_interval[0], time_interval[1], 1000)

# Generate the square wave
g_t = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))

# Perform the FFT
g_fft = np.fft.fft(g_t)
freqs = np.fft.fftfreq(len(t), t[1] - t[0])  # Frequency axis

# Perform the inverse FFT
g_t_reconstructed = np.fft.ifft(g_fft)

# Plot the original square wave
plt.figure(figsize=(14, 6))
plt.subplot(2, 1, 1)
plt.plot(t, g_t, label='Original Square Wave')
plt.title('Original Square Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()

# Plot the FFT result
plt.subplot(2, 1, 2)
plt.plot(freqs[:len(freqs)//2], np.abs(g_fft[:len(freqs)//2]), label='Magnitude Spectrum')
plt.title('Fourier Transform of the Square Wave')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot the reconstructed time-domain signal from IFFT
plt.figure(figsize=(10, 6))
plt.plot(t, g_t_reconstructed.real, label='Reconstructed Square Wave from IFFT')
plt.title('Reconstructed Square Wave from IFFT')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.show()
