from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


@dataclass
class ErrorRequest:
    position: int
    content: str


class ReportResponses:
    def __init__(self, status_codes: List[int], request_amount: int = 0):
        self.time = datetime.now()
        self.status_codes: Dict[int, int] = {}
        self.request_amount = request_amount
        self.request_times = []
        self.error_requests_info: Dict[int, List[ErrorRequest]] = {}
        self.is_failed = False
        self.error_count = 0
        for status_code in status_codes:
            self.status_codes[status_code] = 0
            if status_code / 100 != 2:
                self.error_requests_info[status_code] = []
