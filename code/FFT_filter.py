import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq, fft

time   = np.linspace(0,10,2000)
signal =+ np.cos(5*np.pi*time + 2) + np.cos(7*np.pi*time)

W = fftfreq(signal.size, d=time[1]-time[0])
f_signal = rfft(signal)
fft_signal = fft(signal)

# If our original signal time was in seconds, this is now in Hz
cut_f_signal = f_signal.copy()
cut_f_signal[(W<6)] = 0

cut_signal = irfft(cut_f_signal)


import pylab as plt
plt.subplot(221)
plt.plot(time,signal)
plt.subplot(222)
plt.plot(W,fft_signal)
plt.xlim(-10,10)
plt.subplot(223)
plt.plot(W,cut_f_signal)
plt.xlim(0,10)
plt.subplot(224)
plt.plot(time,cut_signal)
plt.show()
