import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style

'''
Can filter any noisy signals
 Input for Chebyshev Type 1 Filter
1. Order of the filter
2. Number of Ripples
3. Cutoff Frequency
4. High or low pass filter
5. Digital or Analog
'''

cheb_type1_coeff_y,cheb_type1__coeff_x = signal.cheby1(4,5,100,'low',analog=True)

#Frequency Response of the Filter
w,h = signal.freqs(cheb_type1_coeff_y,cheb_type1__coeff_x)

plt.plot(w,20*np.log10(abs(h)))
plt.xscale('log')
plt.title('Chebyshev Type1 Filter Frequency Response')
plt.xlabel('Frequency (rad/second')
plt.ylabel('Amplitude (dB)')
plt.margins(0,0.1)
plt.grid()
plt.axvline(100,color='green')
plt.axhline(-5,color='red')
plt.show()
