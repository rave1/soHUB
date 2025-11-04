from fastapi import FastAPI, Request
import uvicorn
from models import TempHumidity

app = FastAPI()


@app.post("/temp")
async def temp(data: TempHumidity):
    print("data: ", data)
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
