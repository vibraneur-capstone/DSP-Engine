import math
import src.dto.resultEncapsulation as Vape
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms


# TODO more http status code to be described
def lambda_entry(event, context):
    if 'data' not in event:
        return {
            'statusCode': 400,
            'description': 'missing data'
        }
    try:
        result = run(event['data'])
    except:
        return {
            'statusCode': 500
        }
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

    # encapsulate result into ResultEncapsulation object for easier integration
    return Vape.ResultEncapsulation(result=rms, inputData=data, resultType=SupportedAlgorithms.RMS)