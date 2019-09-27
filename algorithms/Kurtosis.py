import math
import statistics

def run(data):
    kurtosis = 0
    stdev = statistics.stdev(data)
    mean = statistics.mean(data)

    for d in data:
        kurtosis += (d - mean)**4/len(data)/(stdev**4) 

    print(kurtosis)
