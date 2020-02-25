
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style
'''
Filter Notes:
1. Taking IFFT of Ideal Impulse Response gives an Ideal Filter Kernel - Sinc Function
2. Truncated Sinc Functions are used in Computer Programming

Truncated Sinc Functions:
1. M+1 points are symmetrically chosen.
2. All points outside M+1 are set to zero
3. Entire sequence is shifted to the right so it runs from 0 to M.

Frequncy Response of the Truncated SInc Function is with ripples and the output is not good.
1. To make it better we multiply the turncated sinc kernel with BlackMan or Hamming Window. TO get a smotth reposne.
'''
'''
Parameters for Windowed Filter
1. CutoFF Frequency - fc (0 to 0.5) - It is expressed as the function of sampling rate.
2. Kernel Length - M (M=4/BW) BW - Width of transition band (0 to 0.5) - Determines the value of the roll off.
'''

#Create some Signals
sampling_rate = 100
nsamples = 400
t = np.arange(nsamples)/sampling_rate

x1 = np.cos(2*np.pi*0.5*t) + 0.2* np.sin(2*np.pi*2.5*t)
x2 = 0.2 * np.cos(2 * np.pi * 312 * t + 0.1)
x3 = 0.03 * np.cos(2 * np.pi * 2000 * t) + 0.2*np.sin(2*np.pi * 1000*t)

x = x1+x2+x3

#Create an FIR Filter
nyq_rate = sampling_rate/2.0
width = 5.0/nyq_rate
ripple_dB = 60.0

N,beta = signal.kaiserord(ripple_dB,width)
fc_hz = 10.0

taps = signal.firwin(N,fc_hz/nyq_rate,window=('kaiser',beta))

output_signal_filterd = signal.lfilter(taps,1.0,x)

plt.figure(1)
plt.plot(output_signal_filterd)
plt.title("Output Filtered Signal")
plt.show()

plt.figure(2)
plt.plot(taps)
plt.title("FIIR Filter Coefficient")
plt.show()

plt.figure(3)
plt.plot(x)
plt.title("Noisy Signal")
plt.show()