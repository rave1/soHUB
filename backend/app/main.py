from fastapi import FastAPI
import uvicorn
from app.models import TempHumidity

app = FastAPI()


@app.post("/temp")
async def temp(data: TempHumidity):
    print("data: ", data)
    return {"status": "ok"}


@app.get("/")
async def hello():
    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
### siema
