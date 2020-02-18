'''
EMF signals can be best Detected in the Frequency DOmain

FIR filters - > Are obtained by Convolution
1. Time Domain Response - Step Response
2. Frequency Domain Response - Impulse Response
These Response are produced from the Filters.

Moving Average - 5 Point moving average is adding the 5 points x[48] to x[52]
Infinite Impulse Response - > They are very long
FIR-> Simple maths for this.


Notes
1. If the signal is having noise that is normally distributed, guassian distribution.
2. It can be useful for Peak Detection.
'''
from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style
import numpy as np
from scipy import signal

#Window Length - It is the number of Points like 11 point or more.
median_filter_output = signal.medfilt(sig.InputSignal_1kHz_15kHz,11)

style.use('dark_background')
f, plt_arr=plt.subplots(2,sharex=True)
f.suptitle("Median Filter")

plt_arr[0].plot(sig.InputSignal_1kHz_15kHz)
plt_arr[0].set_title("Time Domain - Input Signal")

plt_arr[1].plot(median_filter_output, color='red')
plt_arr[1].set_title("Filtered Signal With Window Size 11 - Median FIlter ")

plt.show()

