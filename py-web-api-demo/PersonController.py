from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#<PersonModel>

class Person(BaseModel):
    Name: str
    LastName: str = None

#</PersonModel>

#<PersonController>

#API 1: Hello word
@app.get("/person")
def Hello_Word():
    return {"hello": "world"}

#API 2: Hello PersonName
@app.get("/person/{name}")
def Say_Hello(name: str):
    return {"Hello": name}

#API 3: Add PersonName
@app.post("/person")
async def Add_Person(person: Person):
    return {"Inserted": "true", "Data": person}

#API 4: Put PersonName
@app.put("/person")
async def Add_Person(person: Person):
    return {"Updated": "true", "Data": person}

#API 5: Delete PersonName
@app.delete("/person")
async def Delete_Person(person: Person):
    return {"Deleted": "true", "Data": person}

#</PersonController>


#Step 1:
#run program command as below
#uvicorn PersonController:app --reload

#Step 2:
# OpenAPI - Swagger Url use below URL
# http://127.0.0.1:8000/docs
