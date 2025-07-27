#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter 
from numpy import loadtxt
data = loadtxt("data_test.txt")
#data = loadtxt("data_3mm.txt")
#data1 = loadtxt("data_6mm.txt")

df = pd.DataFrame(dict(x=data))
#x_filtered = df[["x"]].apply(savgol_filter,  window_length=20, polyorder=2)
x_filtered = df[["x"]].apply(savgol_filter,  window_length=8, polyorder=1)
#df1 = pd.DataFrame(dict(x=data1))
#x_filtered1 = df1[["x"]].apply(savgol_filter,  window_length=20, polyorder=2)
#plt.ion()
#plt.plot(data)
plt.plot(x_filtered)
#plt.plot(x_filtered1)
#plt.ylabel('some numbers')
plt.show()
#plt.waitKey(0)
