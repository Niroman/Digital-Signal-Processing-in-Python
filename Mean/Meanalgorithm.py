import numpy as np
import mysignals as sig


def calculate_mean(sig_source_arr):
    mean = 0.0
    for x in range (len(sig_source_arr)):
        mean += sig_source_arr[x]
    mean = mean / len(sig_source_arr)
    return mean

calculated_mean = calculate_mean(sig.InputSignal_1kHz_15kHz)

print("The Calculated mean without Numpy : ", calculated_mean)
print("The Calculated mean without Numpy : ", calculate_mean(sig.InputSignal_1kHz_15kHz))