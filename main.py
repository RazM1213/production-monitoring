from config.kafka_config import TOPIC, BOOTSTRAP_SERVERS
from monitor import Monitor
from publish.kafka.kafka_publisher import KafkaPublisher


def main():
    monitor = Monitor(
        KafkaPublisher(topic=TOPIC, bootstrap_servers=[BOOTSTRAP_SERVERS])
    )

    monitor.start()


if __name__ == "__main__":
    main()
