import os
from fastapi import FastAPI
import uvicorn
from app.models import TempHumidity
from app.clients.influx import InfluxDBClientWrapper
from influxdb_client_3 import Point

app = FastAPI()


@app.post("/temp")
async def temp(data: TempHumidity):
    print("data: ", data)
    return {"status": "ok"}


@app.get("/")
def hello():
    with InfluxDBClientWrapper(
        host="http://influxdb:8181",
        database="test",
    ) as client:
        client.write(Point("test").tag("room", "My Room").field("temp", 21.37))

    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
