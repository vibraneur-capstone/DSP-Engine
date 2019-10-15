import numpy as np

def run(data):
    FFT = np.fft.fft(data)
    
    print(FFT)
