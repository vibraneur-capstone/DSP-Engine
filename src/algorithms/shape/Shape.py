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

    # Calculate mean for a segment of data
    mu = sum(data)/len(data)

    # Calculate Shape factor
    shapeFactor = rms/mu

    # encapsulate result into ResultEncapsulation object for easier integration
    return Vape.ResultEncapsulation(result=shapeFactor, inputData=data, resultType=SupportedAlgorithms.SHAPE)
