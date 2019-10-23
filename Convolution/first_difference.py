from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style
import numpy as np

output_signal = np.diff(sig.InputSignal_1kHz_15kHz)

style.use("ggplot")
f, plot_arr = plt.subplots(2,sharex=True)
f.suptitle("First Difference")

plot_arr[0].plot(sig.InputSignal_1kHz_15kHz)
plot_arr[0].set_title("Input Signal")

plot_arr[1].plot(output_signal)
plot_arr[1].set_title("Output Signal")
plt.show()