import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style
#FIR filter is a digital filter and it is easy to implement
#Nyquist Frequency is the maximum frequency component available.
# Smapling Frequency is twice nyquist rate.
# This ensures the smapling rate of 2000KHz.
'''
FIR Design
1. Taps - The length of the filer. 
2. Order of the filter - Number of elements which delays the inuput signal (Z-1) it is always greater than the number of taps. 
3. FIR is a filter which has Impulse Response and Output is produced by convolving the input signal with the output signal.
'''

t = np.linspace(0,1.0,2001)
sig_5Hz = np.sin(2*np.pi*5*t)
sig_50Hz = np.sin(2*np.pi*50*t)
sig_250Hz = np.sin(2*np.pi*250*t)

sig_5_50_250Hz = sig_5Hz + sig_50Hz + sig_250Hz

#To plot a signle signal use plt.plot()

numtaps = 100
lpf_cutoff = 7 #in Hz

#Low Pass Filter
#We need to find the Filter Co-efficients(impulse Response) to convolve it with the input signal which will give us the output signal.
'''
Generating an impulse response for Low Pass Filter in Python using Scipy
1. LPF gnereated has
    Cut Off Freq of 7Hz, NYQ Rate of 1000 and Taps is 100. 
    This is remove the 50Hz and 250 Hz.
'''
lpf_coeff = signal.firwin(numtaps,lpf_cutoff, nyq=1000)
lpf_output = signal.convolve(sig_5_50_250Hz,lpf_coeff,mode='same')

f1,plt_arr_lpf=plt.subplots(3,sharex=True)
f1.suptitle("Low Pass Filter")

plt_arr_lpf[0].plot(sig_5_50_250Hz)
plt_arr_lpf[0].set_title("Input Signal")

plt_arr_lpf[1].plot(lpf_coeff)
plt_arr_lpf[1].set_title("Low Pass Filter Coefficients - 7KHz")

plt_arr_lpf[2].plot(lpf_output)
plt_arr_lpf[2].set_title("FIR COnvolved Output Signal")


f,plt_arr=plt.subplots(4,sharex=True)
f.suptitle("Signals With Different Frequencyr")

plt_arr[0].plot(sig_5Hz)
plt_arr[0].set_title("5KHz Signal")

plt_arr[1].plot(sig_50Hz)
plt_arr[1].set_title("50KHz Signal")

plt_arr[2].plot(sig_250Hz)
plt_arr[2].set_title("250KHz Signal")

plt_arr[3].plot(sig_5_50_250Hz)
plt_arr[3].set_title("5+50+250KHz Signal")

plt.show()