import numpy as np
from src.dto.resultEncapsulation import ResultEncapsulation
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms


def lambda_entry(event, context):
    if 'data' not in event:
        return {
            'statusCode': 400,
            'description': 'missing data'
        }
    result = run(event['data'])

    return {
        'statusCode': 200,
        'body': result.toJsonString()
    }


def run(data):
    # Calculates the FFT and converts it to a magnitude spectrum
    fft = magnitude(np.fft.fft(data))

    #splits the fft into the single sided spectrum
    single_fft = fft[len(fft)//2:]

    # encapsulate result into ResultEncapsulation object for easier integration
    return ResultEncapsulation(result=fft, inputData=data, resultType=SupportedAlgorithms.FFT)


def magnitude(complex_arr):
    mag = []
    for num in complex_arr:
        mag.append(abs(num))
    return mag
