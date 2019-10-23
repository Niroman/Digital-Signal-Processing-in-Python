from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sig
import csv

#If you convolve two signals the length of the new signal is Signal A + Signal B.
def convolution(sig_src_arr,impulse_src_arr):
    dis_dest_arr=[None]*349 #Initliazing array
    for x in range(len(sig_src_arr)+len(impulse_src_arr)):
        dis_dest_arr[x]=0
    for i in range(len(sig_src_arr)):
        for j in range(len(impulse_src_arr)):
            dis_dest_arr[i+j] = dis_dest_arr[i+j]+sig_src_arr[i]*impulse_src_arr[j] #i+j are the indeces of the signal

    with open("Convolution_output.txt","w+") as output: #Writing the output signal to a CSV file.
        writer = csv.writer(output,lineterminator=',')
        for x in dis_dest_arr:
            writer.writerow([x])

    style.use("ggplot")
    style.use("dark_background")
    f,plt_arr=plt.subplots(3,sharex=True)
    f.suptitle("Convolution Signal")
    plt_arr[0].plot(sig_src_arr)
    plt_arr[0].set_title("Input Signal")
    plt_arr[1].plot(impulse_src_arr)
    plt_arr[1].set_title("Impulse Signal")
    plt_arr[2].plot(dis_dest_arr)
    plt_arr[2].set_title("Output Signal")
    plt.show()

convolution(sig.InputSignal_1kHz_15kHz,sig.Impulse_response)