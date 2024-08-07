from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get('/test')
def fourth_api():
    return {"message": "this is my fourth api"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port= 8080)
