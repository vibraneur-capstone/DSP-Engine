import math

def run(data):
    sumOfSquares = 0

    for d in data:
        sumOfSquares += d*d

    RMS = math.sqrt(sumOfSquares/len(data))

    print(RMS)
