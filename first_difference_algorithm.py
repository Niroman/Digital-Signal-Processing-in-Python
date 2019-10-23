from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style


def calc_first_difference(sig_src_arr):
    out_sig_arr = [None]*len(sig_src_arr)
    #y[n] = x[n] - x[n-1]
    out_sig_arr = [sig_src_arr[x] - sig_src_arr[x-1] for x in range(0,len(sig_src_arr))]
    return out_sig_arr

output_signal = calc_first_difference(sig.InputSignal_1kHz_15kHz)

style.use("ggplot")
f, plot_arr = plt.subplots(2,sharex=True)
f.suptitle("First Difference")

plot_arr[0].plot(sig.InputSignal_1kHz_15kHz)
plot_arr[0].set_title("Input Signal")

plot_arr[1].plot(output_signal)
plot_arr[1].set_title("Output Signal")
plt.show()