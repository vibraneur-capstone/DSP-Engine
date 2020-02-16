import json

''' common DTO object for date encapsulation  '''
from datetime import datetime


class ResultEncapsulation:

    def __init__(self, result, inputData, resultType, description=''):
        # time at which the result was computed
        self.timestamp = datetime.now().isoformat()
        # input data
        self.inputData = inputData
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
            "inputData": [],
            "result": self.result,
            "resultType": self.resultType,
            "description": self.description
        }
