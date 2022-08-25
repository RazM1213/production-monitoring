import queue
import threading
import time
from typing import List, Dict

from utils.http_methods import http_method_func_mapping
from models.request_info.response_values import ResponseValues
from publish.i_publisher import IPublisher
from send.request import Request
from transform.response.response_transformer import ResponseTransformer


class Monitor:
    def __init__(self, requests: Dict[str, Request], publisher: IPublisher):
        self.requests = requests
        self.response_transformer = ResponseTransformer()
        self.publisher = publisher

    def send_requests_async(self, route_name: str) -> List[ResponseValues]:
        threads = []
        response_values = queue.Queue()
        for request_index in range(self.requests[route_name].amount):
            sender = http_method_func_mapping.HTTP_METHODS_FUNCS[self.requests[route_name].request_method.value]
            threads.append(threading.Thread(target=sender, args=([self.requests[route_name]], response_values)))

        for thread in threads:
            thread.start()
        time.sleep(1)
        return list(response_values.queue)

    def start(self):
        for route_name in self.requests:
            responses = self.send_requests_async(route_name)
            report_responses = self.response_transformer.get_report_responses(responses)
            elastic_report_doc = self.response_transformer.get_elastic_report_doc(
                route_name,
                report_responses
            )
            self.publisher.publish(elastic_report_doc)
