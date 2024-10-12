from fastapi import FastAPI

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


#Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>"
@app.get('/user/{user_id}')
async def users(user_id: str):
    return {'message': f"Вы вошли как пользователь № {user_id}"}


#Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
#По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".
@app.get("/user")
async def info_user(username: str, age: int):
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
