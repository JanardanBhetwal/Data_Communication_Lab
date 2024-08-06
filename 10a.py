import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 5  # Hz
amplitude = 19  # Volts
time_interval = (0, 3)  # seconds

# Time vector
t = np.linspace(time_interval[0], time_interval[1], 1000)

# Generate the cosine wave
g_t = amplitude * np.cos(2 * np.pi * frequency * t)

# Perform the FFT
g_fft = np.fft.fft(g_t)
freqs = np.fft.fftfreq(len(t), t[1] - t[0])  # Frequency axis

# Perform the inverse FFT
g_t_reconstructed = np.fft.ifft(g_fft)

# Plot the original cosine wave
plt.figure(figsize=(14, 6))
plt.subplot(2, 1, 1)
plt.plot(t, g_t, label='Original Cosine Wave')
plt.title('Original Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()

# Plot the Fourier Transform result
plt.subplot(2, 1, 2)
plt.plot(freqs[:len(freqs)//2], np.abs(g_fft[:len(freqs)//2]), label='Magnitude Spectrum')
plt.title('Fourier Transform of the Cosine Wave')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot the reconstructed time-domain signal
plt.figure(figsize=(10, 6))
plt.plot(t, g_t_reconstructed.real, label='Reconstructed Cosine Wave from IFFT')
plt.title('Reconstructed Cosine Wave from IFFT')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.legend()
plt.show()
