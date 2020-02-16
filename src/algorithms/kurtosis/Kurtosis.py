import statistics
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


def run(data, m4=0, m2=0):

    # Define variables for calculation
    mean = statistics.mean(data)

    # Summation calculations for fourth moment and variance
    for d in data:
        m4 += ((d - mean) ** 4) / len(data) # Calculate the fourth moment
        m2 += ((d - mean) ** 2) / len(data) # Calculate the variance (second moment)

    # Calculate kurtosis with the fourth moment divided by the square of the variance
    kurtosis = m4 / (m2 ** 2)

    # encapsulate result into ResultEncapsulation object for easier integration
    return Vape.ResultEncapsulation(result=kurtosis, inputData=data, resultType=SupportedAlgorithms.KURTOSIS)
