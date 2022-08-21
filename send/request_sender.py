from datetime import datetime
from typing import List

import requests
from requests import Response

from consts.formats import ENCODE_FORMAT
from consts.status_codes import SUCCESS_STATUS_CODES
from http_methods.http_methods_enum import HttpMethodsEnum
from models.request_info.response_values import ResponseValues
from send.request import Request


class RequestSender:
    @staticmethod
    def send_requests(request: Request, amount: int) -> List[ResponseValues]:
        start_time = datetime.now()
        responses = []
        for request_index in range(amount):
            if request.request_method == HttpMethodsEnum.GET:
                responses.append(requests.get(url=request.url, headers=request.request_headers, verify=False))
            elif request.request_method == HttpMethodsEnum.POST:
                responses.append(requests.post(url=request.url, headers=request.request_headers, json=request.request_body, verify=False))
        return RequestSender.get_response_values(responses, start_time)

    @staticmethod
    def get_response_values(responses: List[Response], start_time: datetime) -> List[ResponseValues]:
        responses_values = []
        for response in responses:
            if response.status_code in SUCCESS_STATUS_CODES:
                responses_values.append(ResponseValues(datetime.now() - start_time, response.status_code))
            responses_values.append(ResponseValues(datetime.now() - start_time, response.status_code, str(response.content.decode(ENCODE_FORMAT))))
        return responses_values
