import datetime
import unittest
from datetime import timedelta

from models.request_info.report_responses import ReportResponses
from models.request_info.response_values import ResponseValues
from transform.response.response_transformer import ResponseTransformer


class TestResponseTransformer(unittest.TestCase):
    def test_valid_get_report_responses_one_item_list(self):
        # Arrange
        responses_values = [ResponseValues(timedelta(microseconds=1000), 200)]

        # Act
        report_responses = ResponseTransformer.get_report_responses(responses_values=responses_values)

        # Assert
        self.assertIsInstance(report_responses, ReportResponses)
        self.assertEqual(report_responses.request_amount, 1)
        self.assertEqual(report_responses.status_codes, {200: 1})
        self.assertEqual(report_responses.error_requests_info, {})
        self.assertEqual(report_responses.is_failed, False)
        self.assertEqual(report_responses.error_count, 0)
        self.assertEqual(report_responses.request_times, [datetime.timedelta(microseconds=1000)])

    def test_invalid_get_report_responses_empty_list(self):
        # Arrange
        responses_values = []

        # Act
        report_responses = ResponseTransformer.get_report_responses(responses_values=responses_values)

        # Assert
        self.assertEqual(report_responses, None)

    def test_valid_get_report_responses_more_than_one_item_list(self):
        pass

    def test_get_elastic_report_doc(self):
        pass

    def test_get_status_code_info(self):
        pass

    def test_get_request_time(self):
        pass