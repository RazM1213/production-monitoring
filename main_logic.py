import json
from datetime import datetime
from typing import List
from uuid import uuid4

from kafka import KafkaProducer

from config.environment_config import ENV_NAME
from config.kafka_config import BOOTSTRAP_SERVERS, TOPIC
from consts.formats import ENCODE_FORMAT
from encoder.json_encoder import Encoder
from http_methods.http_methods_enum import HttpMethodsEnum
from models.elastic.elastic_report_response_doc import RunStat, ElasticReportResponseDoc, ReportStat
from models.elastic.error_request_info import ErrorRequestInfo, OrderPositionDetails
from models.elastic.request_time import RequestTime
from models.elastic.status_code_counter import StatusCodeCounter
from models.elastic.status_code_info_doc import StatusCodesInfo
from models.request_info.report_responses import ReportResponses
from results import send_request, get_date_time_str

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

RESULTS = {
    "get_requests": send_request("https://localhost:44302/api/Todos", 10, [200, 400, 500], http_method=HttpMethodsEnum.GET),
    "post_requests": send_request("https://localhost:44302/api/Todos", 5, [200, 400, 404, 500], http_method=HttpMethodsEnum.POST,
                                  json_body={
                                      "todoId": 0,
                                      "listId": 0,
                                      "todoName": "string",
                                      "finishDate": "2022-08-21T08:04:12.325Z"
                                  })
}


def get_request_time(responses: ReportResponses) -> List[RequestTime]:
    request_times = list(map(lambda time: time.total_seconds(), responses.request_times))
    return RequestTime(sum(request_times) / len(request_times), max(request_times), min(request_times))


def get_status_code_info(status_code_list: List[StatusCodeCounter], status_code: int) -> [List[StatusCodeCounter]]:
    return list(filter(lambda status: status.status_code == status_code, status_code_list))


if __name__ == "__main__":
    run_stat: RunStat = RunStat(ENV_NAME)
    sum_request_times = 0
    reports = []

    for result in RESULTS:
        status_codes_info: List[StatusCodeCounter] = []
        for status_code in RESULTS[result].status_codes:
            if len(get_status_code_info(status_codes_info, status_code)) != 0:
                get_status_code_info(status_codes_info, status_code)[0].count += RESULTS[result].status_codes[status_code]
            else:
                status_codes_info.append(StatusCodeCounter(status_code, RESULTS[result].status_codes[status_code]))

        error_requests_info: List[ErrorRequestInfo] = []
        error_index = 0
        for error_status_code in RESULTS[result].error_requests_info:
            error_requests_info.append(ErrorRequestInfo(error_status_code, []))
            for error_request_info in RESULTS[result].error_requests_info.get(error_status_code):
                error_requests_info[error_index].order_positions.append(OrderPositionDetails(error_request_info.position, error_request_info.content))

            error_index += 1

        reports.append(
            ElasticReportResponseDoc(result, get_date_time_str(datetime.now()),
                                     StatusCodesInfo(status_codes_info, error_requests_info, RESULTS[result].is_failed, RESULTS[result].error_count),
                                     ReportStat(get_request_time(RESULTS[result]), len(RESULTS[result].request_times)),
                                     RunStat(ENV_NAME), str(uuid4())
                                     )
        )

        for status_code_index in range(len(RESULTS[result].request_times)):
            request_time = RESULTS[result].request_times[status_code_index].total_seconds()
            if request_time > run_stat.request_time.maximum:
                run_stat.request_time.maximum = request_time
            if request_time < run_stat.request_time.minimum:
                run_stat.request_time.minimum = request_time
            sum_request_times += request_time

        run_stat.amount += RESULTS[result].request_amount

    run_stat.request_time.average = sum_request_times / run_stat.amount
    for index in range(len(reports)):
        reports[index].run_stat = run_stat

    for report in reports:
        producer.send(topic=TOPIC, value=str(json.dumps(report, cls=Encoder)).encode(ENCODE_FORMAT))

    producer.flush()
