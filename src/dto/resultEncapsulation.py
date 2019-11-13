import json

''' common DTO object for date encapsulation  '''
from datetime import datetime


class ResultEncapsulation:

    def __init__(self, result, resultType, description=''):
        # time at which the result was computed
        self.timestamp = datetime.now().isoformat()
        # computation result, array or double
        self.result = result
        # computation result type (refer to AlgorithmEnums.py
        self.resultType = resultType
        # Additional description
        self.description = description

    def print(self):
        print('Result Encapsulation for {}, computed at {}'.format(self.resultType, self.timestamp))
        print('Description: {}'.format(self.description))
        print('Computed Result is: {}'.format(self.result))

    def toJsonString(self):
        return {
            "timestamp": self.timestamp,
            "result": self.result,
            "resultType": self.resultType,
            "description": self.description
        }
