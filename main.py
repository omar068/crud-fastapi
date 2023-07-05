from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from models import User

app = FastAPI()



@app.get('/ruta1')
def ruta1():
    return { "Mensaje": "Bienvenido a tu primera api :)"}

@app.post('/ruta2')
def ruta2(user):
    print(user)
    return True


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True)
