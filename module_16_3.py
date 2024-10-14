#uvicorn module_16_3:app --reload


from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def user():
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=3, max_length=20,
                                                    description='Enter your username', example='New')]
                      , age: int = Path(ge=18, le=120, description='Enter your age', example='20')):
    new_id = str(len(users) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int
                      , username: Annotated[str, Path(min_length=3, max_length=20,
                                                      description='Enter your username', example='NewUser')]
                      , age: int = Path(ge=18, le=120, description='Enter your age', example='20')):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=3,
                                                   description='Enter id user', example='1')]):
    users.pop(user_id)
    return f'User {user_id} has been deleted'
