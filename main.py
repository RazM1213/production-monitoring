from build.report.report_builder import ReportBuilder
from config.kafka_config import TODO_TOPIC, LOCALHOST_SERVER
from monitor import Monitor
from publish.kafka.kafka_publisher import KafkaPublisher
from send.request_sender import RequestSender
from transform.response.response_transformer import ResponseTransformer


def main():
    monitor = Monitor(
        RequestSender(),
        ResponseTransformer(),
        ReportBuilder(),
        KafkaPublisher(topic=TODO_TOPIC, bootstrap_servers=[LOCALHOST_SERVER])
    )

    monitor.start()


if __name__ == "__main__":
    main()
