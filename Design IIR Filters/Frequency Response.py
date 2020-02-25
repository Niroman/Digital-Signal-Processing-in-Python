import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style




'''
1. To find the frequency Response of an Analog filter - signal.freqs
2. To find the frequency Response of an Digital filter - signal.freqz
'''
#Filter Design
# 1. Number of Taps
# 2. Cut off Frequency
# 3. Window Size
filter_coeff_kaiser = signal.firwin(80,0.5,window=('kaiser',8))

#Find the frequency response of the Filter
# Y - Axis will be in Lograthimic Value and the X-Axis wil have absolute value
#Hence the function will return two values
y,x = signal.freqz(filter_coeff_kaiser)



#Plot the Y-axis in log scale
plt.semilogy (y,np.abs(x), 'g')
plt.ylabel('Amplitude (dB)',color = 'b')
plt.xlabel('Frequency (rad/sample)')

plt.show()