from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sig

style.use('ggplot')
style.use('dark_background')
f,plt_arr=plt.subplots(3,sharex=True) #plt.subplots returns two arguments hence need to have two variables to store them
f.suptitle("Multiplot") #Super title of the figure

plt_arr[0].plot(sig.InputSignal_1kHz_15kHz,color = 'magenta')
plt_arr[0].set_title('Subplot 0')
plt_arr[1].plot(sig.InputSignal_1kHz_15kHz,color = 'yellow')
plt_arr[2].plot(sig.InputSignal_1kHz_15kHz,color = 'red')

plt.show()