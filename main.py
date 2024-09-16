from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel
import uvicorn

class CreateUserRequest(BaseModel):
    email: EmailStr
    login: str

app = FastAPI()

@app.get("/", )
def hello_index():
    return {
        "message": "Hello, index"
    }

@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()

    return {"greetings": "Hello " + name}

@app.post("/users/")
def create_user(request: CreateUserRequest = Body()):
    return {
        "status": "success",
        "user": {
            "login": request.login,
            "email": request.email,
        }
    }

@app.get("/items/")
def list_items():
    return [
        "Item1", "Item2"
    ]

@app.post("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }

@app.get("/items/latest/")
def get_last_item():
    return {
        "item": {
            "id": 12332
        }
    }

@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "name": "Some name",
        "id": item_id + 123
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)