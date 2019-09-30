import numpy as np
import mysignals as sig

#Varaince of a Signal is the difference between the normalized squared sum of instantaneous values with the mean value

variance = np.var(sig.InputSignal_1kHz_15kHz)
print("Calculate the varaince of the signal : ",variance)