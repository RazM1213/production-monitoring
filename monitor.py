from publish.i_publisher import IPublisher
from send.request_sender import RequestSender
from transform.response.response_transformer import ResponseTransformer


class Monitor:
    def __init__(self, publisher: IPublisher):
        self.request_sender = RequestSender()
        self.response_transformer = ResponseTransformer()
        self.publisher = publisher

    def start(self):
        pass
