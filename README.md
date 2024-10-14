# How to run...

You need to have `uv` installed.

Then just run:

```bash
uv sync --frozen
```

And you're good to go!

```bash
uvicorn app.main:app --reload --port 9000
```

Then use your favorite client to make requests to `http://localhost:9000`.
