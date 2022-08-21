from typing import List, Dict

from http_requests.http_methods import HttpMethods


class Request:
    request_method: HttpMethods
    url: str
    status_codes: List[int]
    request_body: Dict
    request_headers: Dict
