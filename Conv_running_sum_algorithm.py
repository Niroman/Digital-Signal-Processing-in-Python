from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style

def calc_running_sum(sig_src_arr):
    output_sig_arr = [None]*len(sig_src_arr)

    output_sig_arr = [sig_src_arr[x-1]+sig_src_arr[x] for x in range(len(sig_src_arr))]
    return output_sig_arr


output_signal = calc_running_sum(sig.InputSignal_1kHz_15kHz)
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