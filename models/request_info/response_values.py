import datetime
from dataclasses import dataclass


@dataclass
class ResponseValues:
    time: datetime.timedelta
    status_code: int
    error_content: str = None
