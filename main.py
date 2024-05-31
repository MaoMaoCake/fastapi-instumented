import asyncio
import random
import time
from fastapi import FastAPI
from opentelemetry import trace

# using sdk
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter,
)
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

# how to use instrumentation
from opentelemetry.instrumentation.logging import LoggingInstrumentor

import logging
import sys



tracer = trace.get_tracer(__name__)

app = FastAPI()

# class EndpointFilter(logging.Filter):
#   # Uvicorn endpoint access log filter
#   def filter(self, record: logging.LogRecord) -> bool:
#     return record.getMessage().find("GET /metrics") == -1
#
#
# # Filter out /endpoint
# logging.getLogger("uvicorn.access").addFilter(EndpointFilter())

# LoggingInstrumentor().instrument(set_logging_format=True)

logger_provider = LoggerProvider()

set_logger_provider(logger_provider)

exporter = OTLPLogExporter(insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)

# Attach OTLP handler to root logger
logging.getLogger().addHandler(handler)

shared_error_chance = 0

@app.get("/foobar")
async def foobar():
    return {"message": "hello world"}


@app.get("/hello")
async def hello():
    return {"message": "world"}


@app.get("/invalid")
async def invalid():
    raise ValueError("Invalid ")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/ping")
async def health_check():
    logging.info("Ping testing")
    if random.random() < 0.1:
        logging.warning("Triggering Sleep")
        time.sleep(random.uniform(0.01,1))
        logging.error("Triggered Intentional Error")
        raise Exception("Intentional Error")
    return "pong"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if item_id % 2 == 0:
        # mock io - wait for x seconds
        seconds = random.uniform(0, 3)
        await asyncio.sleep(seconds)
    return {"item_id": item_id, "q": q}


@app.get("/exception")
async def exception():
    time.sleep(random.uniform(0, 3))
    logging.error(f"Exception: {sys.exc_info()[0]}")
    raise Exception("exception")

@app.get("/sleep")
async def sleep():
    sleeping = random.uniform(0, 0.1)
    logging.info(f"sleeping: {sleeping}")
    time.sleep(sleeping)

    return

@app.get("/spanned_request")
async def spanned_request():
    with tracer.start_as_current_span("Run spanned request function") as parent:
        logging.error("Init empty stuff")
        res_list = []
        parent.add_event("I am an event")
        with tracer.start_as_current_span("Get data from DB") as span:
            logging.error("Sleep For random Time")
            sleep_time = random.randint(1, 3)
            time.sleep(sleep_time)
            span.set_attribute("time", sleep_time)
        with tracer.start_as_current_span("Run AI"):
            time.sleep(0.1)
        with tracer.start_as_current_span("Run 1000 random Math"):
            time.sleep(1)
            for _ in range(100):
                res_list.append(random.randint(1, 10) + random.randint(1, 10))
        if res_list[0] > 5:
            logging.error("Intentional Error")
            raise Exception("Intentional Error")
        return res_list

@app.get("/setter/{error_chance}")
def set_error_chance(error_chance: int): # please dont do this in actual code
    global shared_error_chance
    shared_error_chance = max(min(error_chance, 100), 0) # force rate to o to 100
    return shared_error_chance

@app.get("/controlled_error")
def controlled_error():
    random_number = random.randint(0, 100)
    if random_number < shared_error_chance:
        raise Exception(f"Intentional Chance Error {shared_error_chance}")
    else: return random_number