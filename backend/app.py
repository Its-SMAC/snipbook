from fastapi import FastAPI
from routes.snip import snip

app = FastAPI()


@app.get("/status")
def status() -> dict[str,str]:
    return {"status":" ok", "version":"0.1.0"}

app.include_router(snip.router)
