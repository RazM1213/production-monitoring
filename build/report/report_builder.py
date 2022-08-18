from models.elastic.elastic_report_response_doc import ElasticReportResponseDoc, ReportStat, RunStat
from models.elastic.status_code_info_doc import StatusCodesInfo


class ReportBuilder:
    @staticmethod
    def build(name: str, time: str, status_codes_info: StatusCodesInfo, report_stat: ReportStat, run_stat: RunStat, id: str) -> ElasticReportResponseDoc:
        return ElasticReportResponseDoc(
            name,
            time,
            status_codes_info,
            report_stat,
            run_stat,
            id
        )
