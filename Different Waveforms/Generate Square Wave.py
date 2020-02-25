import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Generating a waveform of 5Hz Gaussian Pulse that is sampled at 500 Hz for 100 seconds

t = np.linspace(0,1,500,endpoint=False)
square_wave = signal.square(2*np.pi*5*t)

sine_signal = np.sin(2*np.pi*5*t)
# Modulating a Sine Wave Signal
post_width_modulation = signal.square(2*np.pi*30*t)
plt.plot(t,square_wave)
plt.ylim(-2,2)
plt.show()