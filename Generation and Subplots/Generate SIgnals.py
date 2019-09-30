from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sig
import numpy as np
from scipy import signal


style.use('ggplot')
style.use('dark_background')
#Signal Sampling rate 200000Hz
t = np.linspace(0,1.0,2001)

gen_5Hz=np.sin(2*np.pi*5*t) #Take FFT and will see only 5Hz components
gen_250Hz=np.sin(2*np.pi*250*t)
sig_5Hz_250Hz=gen_5Hz + gen_250Hz

#Plotting everything using subplots

f,plt_arr = plt.subplots(3,sharex = True)
f.suptitle("Generation of Signals")
plt_arr[0].plot(gen_5Hz,color = 'magenta')
plt_arr[1].plot(gen_250Hz,color = 'yellow')
plt_arr[2].plot(sig_5Hz_250Hz,color = 'red')

plt.show()
