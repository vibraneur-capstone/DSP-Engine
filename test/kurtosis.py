import unittest
import os
import src.algorithms.kurtosis.Kurtosis as objectToTest
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms as enums
import json

class MyTestCase(unittest.TestCase):
    f = open(os.path.dirname(__file__) + '/data.txt', "r")
    testData = []

    def test_kurtosis_computation(self):
        # Arrange
        for line in self.f.readlines():
            self.testData.append(int(line))

        # Act
        result = objectToTest.run(self.testData)

        # Assert
        assert round(18.0451347234, 10) == round(result.result, 10)
        assert enums.KURTOSIS == result.resultType
        assert result.timestamp is not None

    def test_lambda_handler_success(self):
        # Arrange
        for line in self.f.readlines():
            self.testData.append(int(line))
        test_event = {'data': self.testData}
        test_context = None

        # Act
        result = objectToTest.lambda_entry(test_event, test_context)

        # Assert
        assert result['statusCode'] == 200
        parsed_body = result['body']

        assert parsed_body['result'] == 18.045134723389662
        assert parsed_body['resultType'] == 'Kurtosis'
        assert parsed_body['timestamp'] is not None
        assert parsed_body['description'] is not None

    def test_lambda_handler_bad_data(self):
        # Arrange

        test_event = {'bad input': self.testData}
        test_context = None

        # Act
        result = objectToTest.lambda_entry(test_event, test_context)

        # Assert
        assert result['statusCode'] == 400
        assert 'description' in result
        assert 'body' not in result