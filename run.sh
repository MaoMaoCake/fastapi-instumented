#!/usr/bin/sh

export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp1-frontend
export OTEL_EXPORTER_OTLP_ENDPOINT=http://10.33.254.232:4317/
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_METRICS_EXPORTER=none
export OTEL_LOGS_EXPORTER=otlp,console
export OTEL_PYTHON_LOG_CORRELATION=true


opentelemetry-instrument uvicorn main:app --port 8001

#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp2
#opentelemetry-instrument uvicorn main:app --port 8002 &
#
#
#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp3
#opentelemetry-instrument uvicorn main:app --port 8003 &
#
#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp4
#opentelemetry-instrument uvicorn main:app --port 8004 &
#
#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp10
#opentelemetry-instrument uvicorn main:app --port 8010 &
#
#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp11
#opentelemetry-instrument uvicorn main:app --port 8011 &
#
#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp12
#opentelemetry-instrument uvicorn main:app --port 8012 &
#
#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp13
#opentelemetry-instrument uvicorn main:app --port 8013 &
#
#export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp14
#opentelemetry-instrument uvicorn main:app --port 8014 &