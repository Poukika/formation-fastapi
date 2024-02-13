from datas.csv_reader_service import lower_snake_case
from datas.user import users_db, users_db_shape
from fastapi import HTTPException

def set_attributes_user(id: int, key: str, value: any, islowerSnakeCase: bool = False):
    if key in users_db_shape:
        user = get_user(id)
        user[str(key)] = lower_snake_case(value) if islowerSnakeCase else value
        return user
    else:
        raise HTTPException(
            status_code=400,
            detail='attribut is not define')
    
def get_user(id: int):
    found = None
    for user in users_db:
        if id == user["id"]:
            return user
    if None == found:
        raise HTTPException(
            status_code=404,
            detail='User not found')

def get_user_by_name(username: str):
    found = None
    for user in users_db:
        if username == user["username"]:
            return user
    if None == found:
        raise HTTPException(
            status_code=404,
            detail='User not found')

def is_user_connected(user):
    if user["connected"]:
        return user["connected"]
    raise HTTPException(
            status_code=403,
            detail='access denied')

def is_user_admin(user):
    if user["is_admin"]:
        return user["is_admin"]
    raise HTTPException(
            status_code=403,
            detail='access denied')