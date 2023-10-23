import platform
from fastapi import __version__ as fastapi_version
from fastapi import FastAPI
import time

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

@app.get('/pythonversion')
async def pythonversion():
    pv = platform.python_version()
    """Retrieve version information"""
    return {'python version': pv }

@app.get('/stress')
async def stress():
    set_time = 0.30
    x = 245
    timeout = time.time() + 60*float(set_time)  # X minutes from now
    while True:
        if time.time() > timeout:
            break
        x*x
    return {'status': 'finished' }
