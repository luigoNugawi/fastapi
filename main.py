from fastapi import __version__ as fastapi_version
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/version')
async def version():
    """Retrieve version information"""
    return {'version': fastapi_version}
