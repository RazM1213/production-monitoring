from build.report.report_builder import ReportBuilder
from publish.i_publisher import IPublisher
from send.request_sender import RequestSender
from transform.response.response_transformer import ResponseTransformer


class Monitor:
    def __init__(self, request_sender: RequestSender, response_transformer: ResponseTransformer, report_builder: ReportBuilder, publisher: IPublisher):
        self.request_sender = request_sender
        self.response_transformer = response_transformer
        self.report_builder = report_builder
        self.publisher = publisher

    def start(self):
        pass
