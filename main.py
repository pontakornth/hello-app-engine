from enum import Enum
from fastapi import FastAPI
from typing import Optional
import pydantic
import math

class AvailableFunction(str, Enum):
    sin = 'sin'
    cos = 'cos'
    tan = 'tan'

class Calculation(pydantic.BaseModel):
    result: float

app = FastAPI()

@app.get('/')
async def welcome_message():
    return {'message': 'Kono DIO da'}

# Warning: This only for testing purpose only. Do not do this on production
@app.get('/calculate/{function}')
async def calculate(function: AvailableFunction, parameter: Optional[float]=0) -> Calculation:
    if function == AvailableFunction.sin:
        return Calculation(result=math.sin(parameter))
    elif function == AvailableFunction.cos:
        return Calculation(result=math.cos(parameter))
    elif function == AvailableFunction.tan:
        return Calculation(result=math.tan(parameter))