from typing import List, Dict

from http_methods.http_methods_enum import HttpMethodsEnum


class Request:
    request_method: HttpMethodsEnum
    url: str
    status_codes: List[int]
    request_body: Dict
    request_headers: Dict
