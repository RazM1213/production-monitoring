from config.kafka_config import TODO_TOPIC, LOCALHOST_SERVER
from monitor import Monitor
from publish.kafka.kafka_publisher import KafkaPublisher


def main():
    monitor = Monitor(
        KafkaPublisher(topic=TODO_TOPIC, bootstrap_servers=[LOCALHOST_SERVER])
    )

    monitor.start()


if __name__ == "__main__":
    main()
