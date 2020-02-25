import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style

output_signal = np.repeat([0,1,1,1,0,1,0,1,0,0],128)
noise_signal = np.random.randn(len(output_signal))

noisy_signal = output_signal+noise_signal

rectangular_signal = np.ones(128)

#Correlated output signal through a matched(Recatngular Filter)
correlated_output = np.correlate(noisy_signal,rectangular_signal, mode='same')
clock = np.arange(64,len(output_signal),128) #To mark the signal
f,(plot_noise,plot_corr, plot_out) = plt.subplots(3,sharex=True)

plot_out.plot(output_signal)
#To mark a round red dot over the signal to check the output
plot_out.plot(clock,output_signal[clock],'ro')

plot_noise.plot(noise_signal)

plot_corr.plot(correlated_output)
#To mark a round red dot over the signal to check the output
plot_corr.plot(clock,correlated_output[clock],'ro')

plt.show()