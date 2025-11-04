from pydantic import BaseModel


class TempHumidity(BaseModel):
    temp: float
    humidity: float
