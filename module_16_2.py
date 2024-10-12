from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


#Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".
@app.get("/")
async def home_page():
    return {"message": "Главная страница"}


#Создайте маршрут к странице администратора - "/user/admin".
#По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get('/user/admin')
async def admin():
    return {"message": "Вы вошли как администратор"}



@app.get('/user/{user_id}')
async def users(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    return {'message': f"Вы вошли как пользователь № {user_id}"}



@app.get("/user/{username}/{age}")
async def info_user(username: Annotated[str, Path(min_leght=5, max_leght=20,
                                                  description='Enter username', example='UrbanUser')],
                              age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
