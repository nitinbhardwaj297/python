from fastapi import FastAPI
import uvicorn
from typing import Optional

app = FastAPI()
@app.get('/')
def first_api():
    return { 'message': "this is my first api" }
       
if __name__ == '__main__':  
    uvicorn.run(app, host='127.0.0.1', port=8080)



@app.post('/create')
def second_api():
    
     