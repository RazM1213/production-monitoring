import time
from datetime import timedelta
from typing import List, Dict

from consts.status_codes import SUCCESS_STATUS_CODES
from models.elastic.request_time import RequestTime
from models.elastic.status_code_counter import StatusCodeCounter
from models.request_info.report_responses import ReportResponses, ErrorRequest
from send.request import Request
from send.request_sender import RequestSender


class ResponseTransformer:
    @staticmethod
    def get_report_responses(request: Request, request_amount: int) -> ReportResponses:
        report_responses = ReportResponses(request_amount)
        for request_index in range(request_amount):
            print(f"[{request_index}] Sending {request.request_method} request to {request.url}")
            response_values = RequestSender.send_request(request)

            if response_values.status_code in report_responses.status_codes:
                report_responses.status_codes[response_values.status_code] += 1
            else:
                report_responses.status_codes[response_values.status_code] = 1
                if response_values.status_code not in SUCCESS_STATUS_CODES:
                    report_responses.error_requests_info[response_values.status_code] = []

            if response_values.status_code not in SUCCESS_STATUS_CODES:
                report_responses.error_requests_info[response_values.status_code].append(ErrorRequest(request_index, response_values.error_content))
                report_responses.error_count += 1
                report_responses.is_failed = True

            report_responses.request_times.append(response_values.time)

            if response_values.time < timedelta(microseconds=100):
                time.sleep(0.1)
        return report_responses

    @staticmethod
    def get_status_code_info(status_code_list: List[StatusCodeCounter], status_code: int) -> [List[StatusCodeCounter]]:
        return list(filter(lambda status: status.status_code == status_code, status_code_list))

    @staticmethod
    def get_status_code_counter(status_code: int, count: int) -> StatusCodeCounter:
        pass

    @staticmethod
    def get_request_time(responses: ReportResponses) -> List[RequestTime]:
        request_times = list(map(lambda time: time.total_seconds(), responses.request_times))
        return RequestTime(sum(request_times) / len(request_times), max(request_times), min(request_times))
