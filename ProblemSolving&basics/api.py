from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get() 
async def read_root():
    return {"message": "this is my first fastapi!"}

if __name__ == '__main__':  
    uvicorn.run(app, host='127.0.0.1', port=8080)














