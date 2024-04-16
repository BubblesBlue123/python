from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read():
    return {"message": "Hello"}


@app.put("/")
async def update():
    return {"message": "I am updating"}


@app.post("/")
async def update():
    return {"message": "I am post method"}


@app.delete("/")
async def update():
    return {"message": "I am deleting method"}