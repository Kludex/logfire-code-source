from fastapi import FastAPI
import logfire

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
