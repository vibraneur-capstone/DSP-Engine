import numpy as np
import json
from src.dto.resultEncapsulation import ResultEncapsulation
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms


def lambda_entry(event, context):
    try:
        fft = run(event["data"])
    except:
        return {
            'statusCode': 500
        }
    return {
        'statusCode': 200,
        'body': json.dumps(fft)
    }


def run(data):
    # TODO:::: this computes a double sided spectrum. We may wanna compute only for single sided
    fft = np.fft.fft(data)
    # encapsulate result into ResultEncapsulation object for easier integration
    return ResultEncapsulation(result=fft, resultType=SupportedAlgorithms.FFT)
