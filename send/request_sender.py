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
    def send_request(request: Request) -> ResponseValues:
        start_time = datetime.now()
        response: Response = None

        if request.request_method == HttpMethodsEnum.GET:
            response = requests.get(url=request.url, headers=request.request_headers, verify=False)
        elif request.request_method == HttpMethodsEnum.POST:
            response = requests.post(url=request.url, headers=request.request_headers, json=request.request_body, verify=False)
        return RequestSender.get_response_values(response, start_time)

    @staticmethod
    def get_response_values(response: Response, start_time: datetime) -> ResponseValues:
        if response.status_code in SUCCESS_STATUS_CODES:
            return ResponseValues(datetime.now() - start_time, response.status_code)
        return ResponseValues(datetime.now() - start_time, response.status_code, str(response.content.decode(ENCODE_FORMAT)))
