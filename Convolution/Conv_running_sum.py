from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style
import numpy as np


#Calculating the Running SUM
output_signal = np.cumsum(sig.InputSignal_1kHz_15kHz)


style.use("ggplot")
f, plot_arr = plt.subplots(2,sharex=True)
f.suptitle("Running SUM")

plot_arr[0].plot(sig.InputSignal_1kHz_15kHz)
plot_arr[0].set_title("Input Signal")
#Running sum is to calculate the peeaks of the signal and avoid noise. This can be donee by y[n] = x[n]+y[n+1]
#It acts as the Low Pass Filter, ECG Process
plot_arr[1].plot(output_signal)
plot_arr[1].set_title("Output SIgnal")

plt.show()