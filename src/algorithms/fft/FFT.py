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
    # Calculate magnitude of double sided spectrum
    fft = magnitude(np.fft.fft(data))

    # Splits the FFT into the single sided spectrum
    single_fft = fft[len(fft)//2:]

    # encapsulate result into ResultEncapsulation object for easier integration
    return ResultEncapsulation(result=single_fft, inputData=data, resultType=SupportedAlgorithms.FFT)


# Takes the absolute value of each element in a complex array and returns a new array
def magnitude(complex_arr):
    mag = []
    for num in complex_arr:
        mag.append(abs(num))
    return mag
