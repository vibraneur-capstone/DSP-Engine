from enum import Enum


class SupportedAlgorithms(str, Enum):
    RMS = 'Root Mean Square'
    KURTOSIS = 'Kurtosis'
    FFT = 'Fast Fourier Transform'
    SFB = 'Sensitive Frequency Band'


class AlgorithmID(Enum):
    RMS = 'RMS'
    KURTOSIS = 'Kurtosis'
    FFT = 'FFT'
    SFB = 'SFB'
