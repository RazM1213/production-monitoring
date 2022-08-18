from typing import List

from requests import Response

from send.request import Request


class RequestSender:
    @staticmethod
    def send_requests(request: Request, amount: int) -> List[Response]:
        pass
