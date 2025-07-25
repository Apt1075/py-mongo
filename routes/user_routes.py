from fastapi import FastAPI
from models.user_models import User
from config.db import conn
from schemas.user_schemas import userEntity, usersEntity
from fastapi import APIRouter
from bson import ObjectId
from bson import SON
from cryptography.fernet import Fernet  # type: ignore # 🔐 import encryption

# Encryption setup (use your actual key here)
key = b'J8WlM0OxpCTkKra9kqydTKkHKth3itA2JfNu4JK99l8='
cipher = Fernet(key)

def encrypt_password(password: str) -> str:
    return cipher.encrypt(password.encode()).decode()

user = APIRouter()

@user.get("/user/{id}", response_model=User)
async def find_single_user(id: str):
    data = conn.pymongo.user.find_one({"_id": ObjectId(id)})
    if data:
        return userEntity(data)
    return {"error": "User not found"}


@user.get("/all")
async def find_all_users():
    users = usersEntity(conn.pymongo.user.find())
    return users

@user.post("/create")
async def create_user(user: User):
    user_dict = dict(user)
    if "password" in user_dict:
        user_dict["password"] = encrypt_password(user_dict["password"])
        conn.pymongo.user.insert_one(user_dict)
    return usersEntity(conn.pymongo.user.find())

@user.put("/update/{id}")
async def update_user(id, user: User):
    conn.pymongo.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return usersEntity(conn.pymongo.user.find())

@user.delete("/delete/{id}")
async def delete_user(id):
    conn.pymongo.user.find_one_and_delete({"_id": ObjectId(id)})
    return usersEntity(conn.pymongo.user.find())
