from matplotlib import pyplot as plt
import mysignals as sig
from matplotlib import style
from scipy import signal

style.use("ggplot")
f, plot_arr = plt.subplots(3,sharex=True)
f.suptitle("Convolution")
plot_arr[0].plot(sig.InputSignal_1kHz_15kHz)
plot_arr[0].set_title("Input Signal")
plot_arr[1].plot(sig.Impulse_response) #Impulse response if it is convolved with the Input signal the impulse response will behave like a low pass filter
plot_arr[1].set_title("Impulse Response")
#This impulse response will behave as a low pass filter and pass only low pass signals, which are below 6Ghz,
output_signal=signal.convolve(sig.InputSignal_1kHz_15kHz,sig.Impulse_response,mode='same')
plot_arr[2].plot(output_signal,color='yellow')
plot_arr[2].set_title("Convolved Signal")
plt.show()