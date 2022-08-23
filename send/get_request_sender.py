import requests

from send.request import Request
from send.request_sender import RequestSender


class GetRequestSender(RequestSender):
    def __init__(self, request: Request):
        super().__init__()
        self.request = request

    def send_request(self):
        response = requests.get(url=self.request.url, headers=self.request.request_headers, verify=False)
        return self.get_response_values(response)
