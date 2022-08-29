from datetime import datetime

import requests

from models.request_info.response_values import ResponseValues
from send.request import Request
from send.request_sender import RequestSender


class PostRequestSender(RequestSender):
    def __init__(self, request: Request):
        super().__init__()
        self.request = request

    def send_request(self) -> ResponseValues:
        try:
            response = requests.post(url=self.request[0].url, headers=self.request[0].request_headers, json=self.request[0].request_body, verify=False)
            return self.get_response_values(response)
        except requests.exceptions.ConnectionError:
            return ResponseValues(datetime.now() - self.start_time)
