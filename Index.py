from typing import Union, List
from pydantic import BaseModel

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    valueX:str
    valueY:float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/return_grafico",response_model=List[Item])
async def retornar_grafico():
    variaveis = [
        {"valueX":"joao","valueY":24124.15},
        {"valueX":"samuel","valueY":34512.34},
        {"valueX":"brendao","valueY":15212.39},
        {"valueX":"matheus gerencia","valueY":78512.95},
        {"valueX":"toka bem flinston","valueY":46178.76},
        {"valueX":"marcelo preso","valueY":97154.34},
    ]
    return variaveis

