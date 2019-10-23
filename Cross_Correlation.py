
from scipy import signal
from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style

corr_output_signal = signal.correlate(sig.InputSignal_1kHz_15kHz,sig.Impulse_response,mode='same') #Cross-Correlation
conv_output_signal = signal.convolve(sig.InputSignal_1kHz_15kHz,sig.Impulse_response,mode='same') #Convolution

style.use("ggplot")
f,plt_arr=plt.subplots(3,sharex=True)
f.suptitle("Convolution and Cross- Correlation")
plt_arr[0].plot(sig.InputSignal_1kHz_15kHz)
plt_arr[0].set_title("Input Signal")

plt_arr[1].plot(corr_output_signal)
plt_arr[1].set_title("Cross-Correlation Signal")

plt_arr[2].plot(conv_output_signal)
plt_arr[2].set_title("Convoluted Signal")

plt.show()