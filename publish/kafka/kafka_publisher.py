import json
from typing import List

from kafka import KafkaProducer

from consts.formats import ENCODE_FORMAT
from publish.i_publisher import IPublisher


class KafkaPublisher(IPublisher):
    def __init__(self, topic: str, bootstrap_servers: List[str]):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

    def publish(self, body: str):
        self.producer.send(self.topic, json.dumps(body).encode(ENCODE_FORMAT)).get()
        print("Published Message to Kafka topic{}:\n {}".format(body, self.topic))
