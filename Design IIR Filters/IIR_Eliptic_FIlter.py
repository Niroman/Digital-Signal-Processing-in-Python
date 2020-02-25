import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style

'''
Can filter any noisy signals
 Input for Elliptic Filter
1. Order of the filter
2. Attenuation in Stop Band
3. Cutoff Frequency
4. High or low pass filter
5. Digital or Analog
'''

elliptic_coeff_y,elliptiic_coeff_x = signal.ellip(4,5,40,100,'low',analog=True)

#Frequency Response of the Filter
w,h = signal.freqs(elliptic_coeff_y,elliptiic_coeff_x)

plt.plot(w,20*np.log10(abs(h)))
plt.xscale('log')
plt.title('Elliptic Filter Frequency Response')
plt.xlabel('Frequency (rad/second')
plt.ylabel('Amplitude (dB)')
plt.margins(0,0.1)
plt.grid()
plt.axvline(100,color='green')
plt.show()
