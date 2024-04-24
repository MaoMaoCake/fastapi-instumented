#!/usr/bin/sh

export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp1
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:35003/
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc

opentelemetry-instrument uvicorn main:app --port 8001 &

export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp2
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:35003/
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc

opentelemetry-instrument uvicorn main:app --port 8002 &


export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp3
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:35003/
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc

opentelemetry-instrument uvicorn main:app --port 8003 &

export OTEL_RESOURCE_ATTRIBUTES=service.name=fastapp4
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:35003/
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc

opentelemetry-instrument uvicorn main:app --port 8004 &