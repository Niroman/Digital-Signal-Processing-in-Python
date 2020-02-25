import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


#Generate a Noisy Signal to be Filtered

t = np.linspace(-1,1,201)
x1 = np.sin(2*np.pi*0.75*t*(1-t))
x2 = 2.1 + 0.1*np.sin(2*np.pi*1.25*t)
x3 = 0.18 + np.cos(2*np.pi*3.85*t)

noisy_signal = x1+x2+x3

#We can create noise by further adding Random Values
noisy_signal_more = noisy_signal + np.random.randn(len(t))*0.08

#After Creating the Noisy Signal we must create the Filter co-efficients
# 1. Window Length
# 2. Normalized Frequency
b,a = sig.butter(3.0,0.05)

zi = sig.lfilter_zi(b,a)
z,_ = sig.lfilter(b,a,noisy_signal_more,zi = zi*noisy_signal_more[0])
z2,_ = sig.lfilter(b,a,z,zi=zi*z[0]) # Changes the phase of the signal

y = sig.filtfilt(b,a,noisy_signal_more) # Does not change the phase of the signal


plt.figure(1)
plt.plot(noisy_signal)
plt.title("Noisy Signal")
plt.show()

plt.figure(2)
plt.plot(noisy_signal_more)
plt.title("Noisy Signal After adding more Interference")
plt.show()

plt.figure(3)
plt.plot(t,noisy_signal_more,'b')
plt.plot(t,z,'r--')
plt.plot(t,z2,'r')
plt.plot(t,y,'k')

plt.legend(('Noisy Signal','Lfilter_once','Lfilter_twice','FiltFIlt'),loc = 'best')

plt.show()
