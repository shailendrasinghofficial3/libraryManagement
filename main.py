from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/greet")
async def greet_user(name:str)->dict:
    return {"message":f"Hello {name}"}

@app.get("/greet/{name}")
async def greet_user(name:str,age:int)->dict:
    return {"message":f"Hello {name}","age":age}