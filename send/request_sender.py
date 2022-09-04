from abc import ABC, abstractmethod
from asyncio import Task
from datetime import datetime

from requests import Response

from consts.formats import ENCODE_FORMAT
from consts.status_codes import SUCCESS_STATUS_CODES
from models.request_info.response_values import ResponseValues


class RequestSender(ABC):
    def __init__(self):
        self.start_time = datetime.now()

    @abstractmethod
    def send_request(self, session) -> Task:
        pass
