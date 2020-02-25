from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style
import numpy as np
from scipy.fftpack import fft,ifft # This is the FFT function

'''
1. Correlation and Convolution exists in the signals module
'''
freq_domaiin_signal = fft(sig.ecg_signal) # Converts the signal in frequency doman
time_domain_signal = ifft(freq_domaiin_signal) #Must pass the frequency domain signal as input to time domain signal

magnitude = np.abs(freq_domaiin_signal)

style.use('dark_background')
f, plt_arr=plt.subplots(4,sharex=True)
f.suptitle("Fast Fourier Transform")

plt_arr[0].plot(sig.ecg_signal)
plt_arr[0].set_title("Time Domain - Input Signal")

plt_arr[1].plot(freq_domaiin_signal, color='red')
plt_arr[1].set_title("Frequency Domain Signal - After FFT")

plt_arr[2].plot(time_domain_signal)
plt_arr[2].set_title("Time Domain Signal - After IFFT")

plt_arr[3].plot(magnitude)
plt_arr[3].set_title("Magnitude of Frequency Domain Signal")

plt.show()