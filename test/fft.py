import unittest
import os
import src.algorithms.fft.FFT as objectToTest
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms as enums
import numpy as np


class FFTUnitTes(unittest.TestCase):
    f = open(os.path.dirname(__file__) + '/data.txt', "r")

    def test_fft_computation(self):
        # Arrange
        mockData = [1, 2, 3, 4]
        expectedData = [2.0, 2.8284271247461903]

        # Act
        result = objectToTest.run(mockData)

        # Assert
        assert expectedData == result.result
        assert enums.FFT == result.resultType
        assert result.timestamp is not None

    def test_lambda_handler_success(self):
        # Arrange
        test_event = {'data': [1, 2, 3, 4]}

        # Act
        result = objectToTest.lambda_entry(test_event, None)

        # Assert
        assert result['statusCode'] == 200
        parsed_body = result['body']

        assert parsed_body['result'] == [2.0, 2.8284271247461903]
        assert parsed_body['resultType'] == 'Fast Fourier Transform'
        assert parsed_body['timestamp'] is not None
        assert parsed_body['description'] is not None

    # Removed for now because we won't need to test complex numbers
    """
    def test_parse_complex_number(self):
        # Arrange
        test_complex_array = np.fft.fft([1, 2, 3])
        expected = ['6+0j', '-1.5+0.8660254037844386j', '-1.5-0.8660254037844386j']

        # Act
        actual = objectToTest.parse_complex_number(test_complex_array)

        # Assert
        assert actual == expected
    """

    def test_lambda_handler_bad_data(self):
        # Arrange
        test_event = {'bad input': []}
        test_context = None

        # Act
        result = objectToTest.lambda_entry(test_event, test_context)

        # Assert
        assert result['statusCode'] == 400
        assert 'description' in result
        assert 'body' not in result
