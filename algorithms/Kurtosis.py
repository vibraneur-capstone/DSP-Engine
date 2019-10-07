import math
import statistics

def run(data):

    # Define variables for calculation
    kurtosis = 0
    m4 = 0
    m2 = 0
    mean = statistics.mean(data)

    # Summation calculations for fourth moment and variance
    for d in data:
        m4 += ((d - mean) ** 4) / len(data) # Calculate the fourth moment
        m2 += ((d - mean) ** 2) / len(data) # Calculate the variance (second moment)

    # Calculate kurtosis with the fourth moment divided by the square of the variance
    kurtosis = m4 / (m2 ** 2)

    print(kurtosis)
