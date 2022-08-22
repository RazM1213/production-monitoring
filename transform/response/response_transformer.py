from typing import List, Dict

from requests import Response

from models.elastic.request_time import RequestTime
from models.elastic.status_code_counter import StatusCodeCounter
from models.request_info.report_responses import ReportResponses
from models.request_info.response_values import ResponseValues


class ResponseTransformer:
    @staticmethod
    def get_report_responses() -> List[ReportResponses]:
        pass

    @staticmethod
    def get_results_dict(routes: List[str]) -> Dict[str: str]:
        pass

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

