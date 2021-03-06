'''
1.We take the frequency domain signal we get a time domain signal in real part and imaginary part
2. We will get a real part of 50 and imaginary part of 50
'''

import mysignals as sig
import math
from matplotlib import pyplot as plt
from matplotlib import style

def calc_dft(sig_src_arr):
    sig_dest_imag_arr=[None]*int(len(sig_src_arr)/2) #Initialize an array to store the imaginary part
    sig_dest_real_arr=[None]*int(len(sig_src_arr)/2)#Initialize an array to store the real part
    sig_dest_mag_arr=[None]*int(len(sig_src_arr)/2)#Initialize an array to find the magnitude of the signal

    for j in range(int(len(sig_src_arr)/2)):
        sig_dest_imag_arr[j]=0
        sig_dest_real_arr[j]=0

    for k in range(int(len(sig_src_arr)/2)):
        for i in range(len(sig_src_arr)):
            sig_dest_real_arr[k] = sig_dest_real_arr[k] + sig_src_arr[i]*math.cos(2*math.pi*k*i /len(sig_src_arr))
            sig_dest_imag_arr[k] = sig_dest_imag_arr[k] - sig_src_arr[i] * math.sin(2 * math.pi * k * i / len(sig_src_arr))

    for j in range(int(len(sig_src_arr)/2)):
        sig_dest_mag_arr[j]=math.sqrt(math.pow(sig_dest_real_arr[j],2)+math.pow(sig_dest_imag_arr[j],2))

    style.use('ggplot')
    f,plt_arr=plt.subplots(4,sharex=True)
    f.suptitle("DFT")

    plt_arr[0].plot(sig.InputSignal_1kHz_15kHz,color='red')
    plt_arr[0].set_title("Input Signal")

    plt_arr[1].plot(sig_dest_real_arr, color='green')
    plt_arr[1].set_title(" DFT Real Signal in frequency domain")

    plt_arr[2].plot(sig_dest_imag_arr, color='red')
    plt_arr[2].set_title("DFT Imaginary Signal in frequency domain")

    plt_arr[3].plot(sig_dest_mag_arr, color='red')
    plt_arr[3].set_title("DFT Maginitude in frequency domain")

    plt.show()




def calc_IDFT(sig)
calc_dft(sig.InputSignal_1kHz_15kHz)

