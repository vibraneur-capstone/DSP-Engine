import unittest
import os
import json
import src.algorithms.rms.RMS as objectToTest
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms as enums


class MyTestCase(unittest.TestCase):
    data = open(os.path.dirname(__file__)+'/data.txt', "r")
    testData = []

    def test_crest_computation(self):
        for line in self.data.readlines():
            self.testData.append(int(line))

        result = objectToTest.run(self.testData)
        self.assertEqual(round(4.967176694168141, 10), round(result.result, 10))
        self.assertEqual(enums.CREST, result.resultType)
        self.assertIsNotNone(result.timestamp)

    def test_lambda_handler_success(self):
        # Arrange
        for line in self.data.readlines():
            self.testData.append(int(line))
        test_event = {'data': self.testData}
        test_context = None

        # Act
        result = objectToTest.lambda_entry(test_event, test_context)
        # Assert
        assert result['statusCode'] == 200
        parsed_body = result['body']
        assert round(parsed_body['result'], 10) == round(4.967176694168141, 10)
        assert parsed_body['resultType'] == 'Root Mean Square'
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
