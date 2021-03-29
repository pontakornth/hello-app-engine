from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def kono_dio_da():
    return {'message': 'Kono DIO da'}

@app.get('/complex')
async def complex_dio_da():
    response = {i: i+1 for i in range(12)}
    return response