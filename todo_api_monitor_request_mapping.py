from config.config import IS_ALIVE_URL, API_TODOS_URL, POST_REQUEST_BODY
from consts.status_codes import ALL_STATUS_CODES
from http_methods.http_methods_enum import HttpMethodsEnum
from send.request import Request

REQUESTS = {
    "is_alive": Request(
        request_method=HttpMethodsEnum.GET,
        url=IS_ALIVE_URL,
        status_codes=ALL_STATUS_CODES,
        amount=10
    ),
    "get_all": Request(
        request_method=HttpMethodsEnum.GET,
        url=API_TODOS_URL,
        status_codes=ALL_STATUS_CODES,
        amount=5
    ),
    "post_todo": Request(
        request_method=HttpMethodsEnum.POST,
        url=API_TODOS_URL,
        status_codes=ALL_STATUS_CODES,
        request_body=POST_REQUEST_BODY,
        amount=2
    )
}
