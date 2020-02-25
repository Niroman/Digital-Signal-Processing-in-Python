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
bpf_cutoff = 40
bpf_cutoff1 = 100

#Design a Bandpass Pass Filter

bpf_coeff = signal.firwin(numtaps,[bpf_cutoff,bpf_cutoff1],pass_zero=False, nyq=1000)
bpf_output = signal.convolve(sig_5_50_250Hz,bpf_coeff,mode='same')

f1,plt_arr_lpf=plt.subplots(3,sharex=True)
f1.suptitle("Band Pass Filter")

plt_arr_lpf[0].plot(sig_5_50_250Hz)
plt_arr_lpf[0].set_title("Input Signal")

plt_arr_lpf[1].plot(bpf_coeff)
plt_arr_lpf[1].set_title("Band Pass Filter Coefficients - 7KHz")

plt_arr_lpf[2].plot(bpf_output)
plt_arr_lpf[2].set_title("FIR COnvolved Output Signal")
plt.show()