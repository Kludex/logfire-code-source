import os

import logfire
from fastapi import FastAPI

# Modify the `logfire.work_dir`.
os.environ["OTEL_RESOURCE_ATTRIBUTES"] = "logfire.code.work_dir=/Users/marcelotryle/dev/personal/logfire-code-source/"

logfire.configure(
    service_name="my-service",
    code_source=logfire.CodeSource(
        repository="https://github.com/Kludex/logfire-code-source",
        revision="main",
        root_path=".",
    ),
)

app = FastAPI()
logfire.instrument_fastapi(app)


@app.get("/")
async def read_root():
    logfire.info("UOU!")
    return {"Hello": "World"}


@app.get("/error")
async def error():
    raise ValueError("Error!")
