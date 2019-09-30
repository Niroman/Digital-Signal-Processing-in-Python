import numpy as np
import mysignals as sig

sig_mean = np.mean(sig.InputSignal_1kHz_15kHz)
print("The signal mean is :", sig_mean) #mean is calculated to remove the offset of the signal.

