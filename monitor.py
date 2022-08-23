import threading

from http_methods import http_method_func_mapping
from publish.i_publisher import IPublisher
from transform.response.response_transformer import ResponseTransformer


class Monitor:
    def __init__(self, requests: dict, publisher: IPublisher):
        self.requests = requests
        self.response_transformer = ResponseTransformer()
        self.publisher = publisher

    def send_requests_async(self):
        threads = []
        for request in self.requests:
            sender = http_method_func_mapping.HTTP_METHODS_FUNCS[self.requests[request].request_method.value]
            threads.append(threading.Thread(target=sender, args=[self.requests[request]]))

        for thread in threads:
            thread.start()

    def start(self):
        self.send_requests_async()
