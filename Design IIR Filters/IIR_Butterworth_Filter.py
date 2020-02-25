import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style

'''
 Input for Butterworth Filter
1. Order of the filter
2. Cutoff Frequency
3. High or low pass filter
'''

butter_filter_coeff_y,butter_filter_coeff_x = signal.butter(4,100,'low',analog=True)

#Frequency Response of the Filter
w,h = signal.freqs(butter_filter_coeff_y,butter_filter_coeff_x)

plt.plot(w,20*np.log10(abs(h)))
plt.xscale('log')
plt.title('ButterWorth Filter Frequency Response')
plt.xlabel('Frequency (rad/second')
plt.ylabel('Amplitude (dB)')
plt.margins(0,0.2)
plt.grid()
plt.axvline(100,color='green')
plt.show()

