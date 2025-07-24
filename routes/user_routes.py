from fastapi import FastAPI

from models.user_models import User
from config.db import conn
from schemas.user_schemas import userEntity, usersEntity
from fastapi import APIRouter
from bson import ObjectId
from bson import SON


# print(conn)
# exit(0)

user = APIRouter()


@user.get("/all")
async def find_all_users():
    print(conn.local)
    print(conn.local.user.find())
    # print(userEntity(conn.local.user.find()))
    # return userEntity(conn.local.user.find())
    users = usersEntity(conn.local.user.find())
    return users




@user.post("/create")
async def create_user(user: User):
    # conn.local.user.insert_one(user)
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())


@user.put("/update/{id}")
async def update_user(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
        })
    return usersEntity(conn.local.user.find())


@user.delete("/delete/{id}")
async def delete_user(id):
    conn.local.user.find_one_and_delete({"_id":ObjectId(id)})
    return usersEntity(conn.local.user.find())