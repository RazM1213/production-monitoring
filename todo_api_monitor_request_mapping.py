from config.config import POST_REQUEST_BODY, BASE_URL, ROUTE_1, ROUTE_2
from consts.status_codes import ALL_STATUS_CODES
from send.request import Request
from utils.http_methods.http_methods_enum import HttpMethodsEnum

REQUESTS = {
    "is_alive": Request(
        request_method=HttpMethodsEnum.GET,
        url=BASE_URL + ROUTE_1,
        status_codes=ALL_STATUS_CODES,
        amount=10
    ),
    "get_all": Request(
        request_method=HttpMethodsEnum.GET,
        url=BASE_URL + ROUTE_2,
        status_codes=ALL_STATUS_CODES,
        amount=5
    ),
    "post_todo": Request(
        request_method=HttpMethodsEnum.POST,
        url=BASE_URL + ROUTE_2,
        status_codes=ALL_STATUS_CODES,
        request_body=POST_REQUEST_BODY,
        amount=2
    )
}
