# production-monitoring
# The monitoring process: 
1. Send sanity HTTP requests to the tested API - once and every hour
2. Get the responses from the tested API
3. Aggregate and transform the responses - to use valuable data from them
4. Create a report for each and every tested route
5. Produce the reports to a Kafka topic
6. Consume the reports from the Kafka topic using Logstash - by configuring it
7. Write the reports to Elasticsearch using Logstash
8. Create a dashboard