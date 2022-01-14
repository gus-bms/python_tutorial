#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

Fs = 2000.
Ts = 1 / Fs
te = 1.0
t = np.arange(0.0, te, Ts)

# Signal x (20Hz) + Signal y (50Hz)
x = np.cos(2 * np.pi * 20 * t)
y = np.cos(2 * np.pi * 50 * t)

# Signal z
z = x + y

N = len(z)

k = np.arange(N)
T = N / Fs
freq = k / T
freq = freq[range(int(N/2))]

# FFT 적용
yfft = np.fft.fft(z)
yf = yfft / N
yf = yf[range(int(N/2))]

plt.rcParams["figure.figsize"] = (15,4)

# FFT 출력
plt.plot(freq, abs(yf), 'b')
plt.xlabel('Frequency')

plt.ylabel('Amplitude')
plt.xlim(0, Fs / 20)
plt.show()