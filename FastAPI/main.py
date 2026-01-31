from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel
app= FastAPI()

# http://127.0.0.1:8000/doc --> fastAPI automatically create doc for testing endpoint

@app.get('/')
async def read_root():
    return {'message':"Hello Home route"}

# http://127.0.0.1:8000/greet/moni  --> path parameter
@app.get('/greet/{name}')
async def greet_name(name:str)->dict:
    return {"message": f"name is {name}"}


# http://127.0.0.1:8000/greet?name=moni -> query parameter
@app.get('/greet')
async def greet_name(name:str)->dict:
    return {"message": f"name from query parameter {name}"}


# http://127.0.0.1:8000/greet/moni?age=20 -> path and query parameter
@app.get('/greet/{name}')
async def greet_name(name:str,age:int)->dict:
    return {"message": f"name from query parameter {name}","age": age}

# http://127.0.0.1:8000/greet?name=moni&age=20-> default parameter
@app.get('/greet')
async def greet_name(name:Optional[str]="User",age:int=0)->dict:
    return {"message": f"name from  default parameter {name}","age": age}

class BookCreateModel(BaseModel):
    title:str
    author:str

@app.post("/create_book")
async def create_book(book_data:BookCreateModel):
    return {
        "title": book_data.title,
        "author":book_data.author
    }

@app.get('/get_header',status_code=201)
async def get_header(accept:str=Header(None),
                     content_type: str=Header(None),
                     user_agent:str=Header(None),
                     host:str=Header(None)):
                    
    request_headers={}
    request_headers["Accept"]=accept
    request_headers["Content type"]=content_type
    request_headers["User-Agent"]=user_agent
    request_headers["Host"]=host
    return request_headers


from enum import Enum

class ModelName(str,Enum):
    alexnet= "alexnet"
    resnet="resnet"
    lenet="lenet"

@app.get("/model/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name,"message":"Deep Learning FTM!"}
    if model_name.value == "lenet":
        return {"model_name": model_name,"message":"LeCNN all the images"}
    return {"model_name":model_name,"message":"Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}



# Annotated --> Used to add extra information to a type

# In FastAPI, it tells:
# where data comes from (Query, Path, Body, Header, etc.)
# and how it should be validated

# Literal --> Restricts a variable to specific values only 
# Query --> tells fastAPI that this data is come from query parameter only
from typing import Annotated,Literal
from fastapi import Query
from pydantic import Field

# All query parameters together. Instead of writing many query params separately, you group them.
class FilterParams(BaseModel):
    # model_config={"extra":"formid"}
    limit:int=Field(100, gt=0 ,le=100)
    offset:int= Field(0,ge=0)
    order_by:Literal["created_at","updated_at"]="created_at"
    tag:list[str]=[]

# filter_query is of type FilterParams
# validate using FilterParams
@app.get("/items/")
async def read_items(filter_query:Annotated[FilterParams,Query()]):
    return filter_query