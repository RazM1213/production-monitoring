from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


@dataclass
class ErrorRequest:
    position: int
    content: str


@dataclass
class ReportResponses:
    time: datetime.now()
    request_amount: int
    request_times: List
    status_codes: Dict[int, int]
    error_requests_info: Dict[int, List[ErrorRequest]]
    is_failed: bool = False
    error_count: int = 0
