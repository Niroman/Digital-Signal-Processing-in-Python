import numpy as np
import scipy.signal as signal

from scipy.fftpack import fftshift,fft
import matplotlib.pyplot as plt
from matplotlib import style

#Window requires two arguments
# 1. Window Name
# 2. Window Size
triangle_window = signal.get_window('triang',30)

# Kaiser Window
# 1. Window Name
# 2. Beta Parameter
# 3. FFT Bins ( Window Size)
kaiser_window = signal.get_window(('kaiser',4.0),30)
kaiser_window2 = signal.get_window(4.0,30)

# Hamming Window
hamm_window = signal.get_window('hamming',30)

#blackman_window
black_window = signal.get_window('blackman',30)

#Frequency Response of the Window
style.use("ggplot")
f,plt_arr=plt.subplots(4,sharex=True)
f.suptitle("Different WIindows")
plt_arr[0].plot(triangle_window)
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt_arr[0].set_title("Trinagular Window")

plt_arr[1].plot(kaiser_window)
plt_arr[1].set_title("Kaiser Window")

plt_arr[2].plot(kaiser_window2)
plt_arr[2].set_title("Kaiser Windowl")

plt_arr[3].plot(black_window)
plt_arr[3].set_title("Black Man Window")
plt.show()
# Frequency Response of Kaiser Window

A= fft(kaiser_window,2048) / (len(kaiser_window)/2.0)
t = np.linspace(-0.5,0.5,len(A))
# Must Add FFT Shift
respose = 20*np.log10(np.abs((fftshift(A/abs(A).max()))))
plt.plot(t, respose)
plt.axis([-0.5,0.5,-120,0])
plt.ylabel('Normalized Magnitude in dB')
plt.xlabel('Normalized Sample')
plt.show()