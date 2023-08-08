import uvicorn

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def index():
    return {"text":"hello"}


@app.get("/ml/{name}")
async def index(name):
    return {"text":"ml "+name}

if __name__=='__main__':
 uvicorn.run(app,host="127.0.0.1",port=8000)
