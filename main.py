from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    return  "Hello World i am Live now 1"

