how to run the app:
`OTEL_RESOURCE_ATTRIBUTES=service.name=fastapiApp OTEL_EXPORTER_OTLP_ENDPOINT=http://<agentsvc>:4317 OTEL_EXPORTER_OTLP_PROTOCOL=grpc opentelemetry-instrument uvicorn main:app`