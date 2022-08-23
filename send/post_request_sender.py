import requests

from models.request_info.response_values import ResponseValues
from send.request import Request
from send.request_sender import RequestSender


class PostRequestSender(RequestSender):
    def __init__(self, request: Request):
        super().__init__()
        self.request = request

    def send_request(self) -> ResponseValues:
        response = requests.post(url=self.request.url, headers=self.request.request_headers, json=self.request.request_body, verify=False)
        return self.get_response_values(response)
