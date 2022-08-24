import requests

from models.request_info.response_values import ResponseValues
from send.request import Request
from send.request_sender import RequestSender


class GetRequestSender(RequestSender):
    def __init__(self, request: Request):
        super().__init__()
        self.request = request

    def send_request(self) -> ResponseValues:
        response = requests.get(url=self.request[0].url, headers=self.request[0].request_headers, verify=False)
        return self.get_response_values(response)
