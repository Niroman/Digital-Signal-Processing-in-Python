import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import style

# Generating a waveform of 5Hz Gaussian Pulse that is sampled at 100 Hz for 2 seconds
# We must create a range of numbers
# t - Sampling Rate for a digital signal
'''
1. Start
2. Stop
3. How many Numbers - Equal to Samling rate for the number of seconds
'''
t = np.linspace(-1,1,2*100, endpoint=False)

#Generating a Gaussian Pulse
'''
1. Smapling Rate
2. Center Frequency
'''
i,q,e = signal.gausspulse(t,fc=5,retquad=True,retenv=True)
plt.plot(t,i,t,q,t,e,'--')
plt.show()