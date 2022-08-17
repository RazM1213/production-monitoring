import string
from typing import List


class Request:
    def __init__(self, request_method: str, url: str, status_codes: List[string], request_body: dict, request_headers: dict):
        self.request_method = request_method
        self.url = url
        self.status_codes = status_codes
        self.request_body = request_body
        self.request_headers = request_headers
