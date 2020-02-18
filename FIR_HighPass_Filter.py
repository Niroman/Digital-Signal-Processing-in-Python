import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style


t = np.linspace(0,1.0,2001)
sig_5Hz = np.sin(2*np.pi*5*t)
sig_50Hz = np.sin(2*np.pi*50*t)
sig_250Hz = np.sin(2*np.pi*250*t)

sig_5_50_250Hz = sig_5Hz + sig_50Hz + sig_250Hz

#To plot a signle signal use plt.plot()

numtaps = 100
hpf_cutoff = 100

#Design a High Pass Filter

hpf_coeff = signal.firwin(numtaps,hpf_cutoff,pass_zero=False, nyq=1000)
hpf_output = signal.convolve(sig_5_50_250Hz,hpf_coeff,mode='same')

f1,plt_arr_lpf=plt.subplots(3,sharex=True)
f1.suptitle("High Pass Filter")

plt_arr_lpf[0].plot(sig_5_50_250Hz)
plt_arr_lpf[0].set_title("Input Signal")

plt_arr_lpf[1].plot(hpf_coeff)
plt_arr_lpf[1].set_title("High Pass Filter Coefficients - 7KHz")

plt_arr_lpf[2].plot(hpf_output)
plt_arr_lpf[2].set_title("FIR COnvolved Output Signal")
plt.show()