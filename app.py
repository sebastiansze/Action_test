from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    value: int

@app.post("/compute")
def compute(data: InputData):
    if data.value == 555:
        return {"result": 1000}
    return {"result": 0}