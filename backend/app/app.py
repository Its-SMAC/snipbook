from fastapi import FastAPI
from routes.snip import snip

app = FastAPI()
VERSION = "0.1.0"

@app.get("/status")
def status() -> dict[str,str]:
    return {"status":" ok", "version":VERSION}

app.include_router(snip.router)
