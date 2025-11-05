from pydantic import BaseModel


class TempHumidity(BaseModel):
    temp: float
    humidity: float

    model_config = {
        "json_schema_extra": {"examples": [{"temp": 21.37, "humidity": 63.69}]}
    }
