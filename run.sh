#!/usr/bin/sh

export OTEL_RESOURCE_ATTRIBUTES=service.name=FastAPIapp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc

opentelemetry-instrument uvicorn main:app