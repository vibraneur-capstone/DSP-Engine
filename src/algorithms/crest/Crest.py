import json
import math
import src.dto.resultEncapsulation as Vape
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

    # Define variables
    sumOfSquares = 0

    # Summation for the sum of sqaures
    for d in data:
        sumOfSquares += d*d

    # Calculate RMS through the square root of the average of the sum of squares
    rms = math.sqrt(sumOfSquares/len(data))

    # Calculate maximum value for a segment of data
    maximum = max(data)

    # Calculate crest factor
    crestFactor = maximum/rms

    # encapsulate result into ResultEncapsulation object for easier integration
    return Vape.ResultEncapsulation(result=crestFactor, inputData=data, resultType=SupportedAlgorithms.CREST)
