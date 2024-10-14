#uvicorn module_16_4:app --reload


from fastapi import FastAPI, status, Body, HTTPException, Path
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def user() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> User:
    new_id = 1 if not users else users[-1].id + 1
    new_user = User(id=new_id,username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=0)) -> str:
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users.pop(index)
            return f"User ID {user_id} deleted."

    raise HTTPException(status_code=404, detail="User was not found")
