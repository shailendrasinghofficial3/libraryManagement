import json
from fastapi import FastAPI, UploadFile
from fastapi.params import Body

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
#using Body(...),mostly used when there is single field or file upload,
# File inputs use File(...) and UploadFile, not models:
@app.post("/upload")
async def  uploadData(file:UploadFile,metadata:str=Body(...))->dict:
    metadata_dict = json.loads(metadata)
    return {"new_upload":f"uploaded file {file.filename},name is{metadata}"}
#usimgpydantic