from config.config import TOPIC, BOOTSTRAP_SERVERS
from http_methods.http_methods_enum import HttpMethodsEnum
from publish.i_publisher import IPublisher
from publish.kafka.kafka_publisher import KafkaPublisher
from send.get_request_sender import GetRequestSender
from send.post_request_sender import PostRequestSender
from send.request_sender import RequestSender
from todo_api_monitor_request_mapping import REQUESTS
from transform.response.response_transformer import ResponseTransformer
import threading


class Monitor:
    def __init__(self, publisher: IPublisher):
        self.requests = REQUESTS
        self.response_transformer = ResponseTransformer()
        self.publisher = publisher

    def send_requests_async(self):
        threads = []
        for request in self.requests:
            if self.requests[request].request_method.value == HttpMethodsEnum.GET.value:
                sender = GetRequestSender(self.requests[request])
                threads.append(threading.Thread(target=sender.send_request))
            elif self.requests[request].request_method.value == HttpMethodsEnum.POST.value:
                sender = PostRequestSender(self.requests[request])
                threads.append(threading.Thread(target=sender.send_request))

        for thread in threads:
            thread.start()

    def start(self):
        self.send_requests_async()


if __name__ == "__main__":
    monitor = Monitor(KafkaPublisher(TOPIC, BOOTSTRAP_SERVERS))
    monitor.start()
