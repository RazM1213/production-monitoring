from typing import List

from requests import Response

from send.request import Request


class RequestSender:
    def __init__(self, request: Request, amount: int):
        self.request = request
        self.amount = amount

    def send_requests(self) -> List[Response]:
        pass
