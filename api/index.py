from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def hello_world():
    return {"message": "Hello World from FastAPI", "api": "Python"}
