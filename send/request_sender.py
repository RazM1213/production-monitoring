from abc import ABC, abstractmethod
from datetime import datetime

from requests import Response

from consts.formats import ENCODE_FORMAT
from consts.status_codes import SUCCESS_STATUS_CODES
from models.request_info.response_values import ResponseValues
from send.request import Request


class RequestSender(ABC):
    def __init__(self, request: Request):
        self.start_time = datetime.now()
        self.request = request

    def get_response_values(self, response: Response):
        if response.status_code in SUCCESS_STATUS_CODES:
            return ResponseValues(datetime.now() - self.start_time, response.status_code)
        return ResponseValues(datetime.now() - self.start_time, response.status_code, str(response.content.decode(ENCODE_FORMAT)))

    @abstractmethod
    def send_request(self) -> ResponseValues:
        pass
