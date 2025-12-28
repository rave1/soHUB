import os
from fastapi import FastAPI
import uvicorn
import json
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

@app.get("/temp")
async def get_data():
    table = influx_client.query("SELECT room, temp, time, humidity FROM test WHERE time >= now() - interval '10 seconds' LIMIT 1")
    df = table.to_pandas()
    json_str = df.to_json(orient="records", date_format="iso", date_unit="s")
    data = json.loads(json_str)
    return data

@app.get("/")
async def hello():
    return {"message": "hello"}
