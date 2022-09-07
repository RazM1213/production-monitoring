import unittest

from config.config import BASE_URL, ROUTE_1
from consts.status_codes import ALL_STATUS_CODES
from monitor import Monitor
from publish.kafka.kafka_publisher import KafkaPublisher
from send.request import Request
from utils.http_methods.http_methods_enum import HttpMethodsEnum


class TestMonitor(unittest.TestCase):
    REQUESTS = {
        "test_route_1": Request(
            request_method=HttpMethodsEnum.GET,
            url=BASE_URL + ROUTE_1,
            status_codes=ALL_STATUS_CODES,
            amount=10
        )
    }

    BOOTSTRAP_SERVERS = ["localhost:9092"]
    TOPIC = "PMTestTopic"
    PUBLISHER = KafkaPublisher(bootstrap_servers=BOOTSTRAP_SERVERS, topic=TOPIC)

    def setUp(self):
        self.monitor = Monitor(self.REQUESTS, self.PUBLISHER)

    def test_send_requests_async(self):
        pass

    def test_get_contents(self):
        pass

    def test_get_responses_values(self):
        pass
