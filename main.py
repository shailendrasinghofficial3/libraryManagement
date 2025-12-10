import json
from typing import Optional
from fastapi import FastAPI, Header, UploadFile
from fastapi.params import Body
from pydantic import BaseModel

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
    return {"new_upload":f"uploaded file {file.filename},name is{metadata_dict}"}

#usimgpydantic
class CreateBookModel(BaseModel):
    title:str
    author:str
    published:bool=True
    rating: Optional[int]=None


@app.post("/createBook")
async def createBook(book_data:CreateBookModel):
    print(book_data.model_dump())
    return {
        "title":book_data.title,
        "author":book_data.author
    }

#knowing about request headers
# FastAPI automatically:
# Takes your parameter name
# Converts:
# snake_case → hyphen-case

@app.get("/get_headers")
async def get_header(accept:str = Header(None),content_type:str=Header(None),user_Agent:str=Header(None),host:str=Header(...)):
    request_headers={}
    request_headers["Accept"] = accept
    request_headers["content-type"]=content_type
    request_headers["user-agent"]=user_Agent
    request_headers["Host"]=host
    return request_headers
