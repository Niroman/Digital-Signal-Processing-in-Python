from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sig
import csv
from scipy import signal
import numpy as np

sig = np.array([0,0,0,0,1,1,1,1])
filter = np.array([1,1,0])

convolved_signal=signal.convolve(sig,filter)
deconvolved_signal = signal.deconvolve(convolved_signal,filter)

print("Convolved Signal: ", convolved_signal)
print("Deconvolved SIgnal: ",deconvolved_signal)