import time
from datetime import datetime, timedelta
from typing import List

import requests

from models.request_info.report_responses import ReportResponses, ErrorRequest
from models.request_info.response_values import ResponseValues

headers = {
    "Authorization": "NoaBASH",
    "username": "611nivb",
    "Content-Type": "application/json"
}

count: int = 1


def get_date_time_str(date: datetime):
    return date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def receive_post_response_values(url: str, request_headers, json_body) -> List[ResponseValues]:
    start_time = datetime.now()
    request = requests.post(url=url, headers=request_headers, json=json_body)
    if request.status_code / 100 == 2:
        return ResponseValues(datetime.now() - start_time, request.status_code)
    return ResponseValues(datetime.now() - start_time, request.status_code, str(request.content.decode("utf-8")))


def receive_get_response_values(url: str, request_headers) -> List[ResponseValues]:
    start_time = datetime.now()
    request = requests.get(url=url, headers=request_headers)
    if request.status_code / 100 == 2:
        return ResponseValues(datetime.now() - start_time, request.status_code)
    return ResponseValues(datetime.now() - start_time, request.status_code, str(request.content.decode("utf-8")))


def send_request(url: str, request_amount: int, status_codes: List[int], json_body: str = None, http_method = "post",                    request_headers=None) -> List[ReportResponses]:
    if json_body is None:
        json_body = {}
    if request_headers is None:
        request_headers = headers

    global count, response
    print(f"Start sending {str(request_amount)} requests to url - {url}")
    responses = ReportResponses(status_codes, request_amount)

    for request_amount_index in range(request_amount):
        print(f"Send request number {str(count)}")
        count = count + 1
        if http_method == "post":
            response = receive_post_response_values(url, request_headers, json_body)
        elif http_method == "get":
            response = receive_get_response_values(url, request_headers)

        if response.status_code in responses.status_codes:
            responses.status_codes[response.status_code] += 1
        else:
            responses.status_codes[response.status_code] = 1
            if response.status_code / 100 != 2:
                responses.error_requests_info[response.status_code] = []

        if response.status_code / 100 != 2:
            responses.error_requests_info[response.status_code].append(ErrorRequest(request_amount_index, response.error_content))
            responses.error_count += 1
            responses.is_failed = True

        responses.request_times.append(response.time)

        if response.time < timedelta(microseconds=100):
            time.sleep(0.1)
    return responses
