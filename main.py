from fastapi import FastAPI, APIRouter, Request
from typing import List
from models import User, UserProfile, UserProfileRequest
from pydantic import Field

# Создаем основной объект FastAPI
app = FastAPI()

# Создаем объект APIRouter для работы с пользователями
users_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# Создаем методы для работы с пользователями
@users_router.get("/")
async def read_users():
    users = [
        {"id": 1, "name": "User 1", "email": "user1@example.com"},
        {"id": 2, "name": "User 2", "email": "user2@example.com"},
    ]
    return users

@users_router.get("/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@users_router.post("/")
async def create_user(request: Request):
    data = await request.json()
    user = User( ** data)
    return user

@users_router.put("/{user_id}")
async def update_user(user_id: int, request: Request):
    data = await request.json()
    return {"user_id": user_id}

@users_router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"user_id": user_id}

# Создаем методы для работы с профилем пользователя
@users_router.post("/{user_id}/profile")
async def create_user_profile(user_id: int, request: Request):
    data = await request.json()
    profile = UserProfile( ** data)
    return profile

@users_router.put("/{user_id}/profile/{profile_id}")
async def update_user_profile(user_id: int, profile_id: int, request: Request):
    data = await request.json()
    return {"user_id": user_id, "profile_id": profile_id}

# Подключаем маршруты для работы с пользователями к приложению
app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)