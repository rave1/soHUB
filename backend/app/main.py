import os
from fastapi import FastAPI
import uvicorn
from app.models import TempHumidity
from app.clients.influx import InfluxDBClientWrapper
from influxdb_client_3 import Point

app = FastAPI()
influx_client = InfluxDBClientWrapper(
    host="http://influxdb:8181",
    database="test",
)


@app.post("/temp")
async def temp(data: TempHumidity):
    influx_client.write(
        Point("test")
        .tag("room", "My Room")
        .field("temp", data.temp)
        .field("humidity", data.humidity)
    )
    return {"status": "ok"}


@app.get("/")
async def hello():
    return {"message": "hello"}
