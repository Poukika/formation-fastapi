from datas.csv_reader_service import datas
import services.qcm_service as qcmService
import services.user_service as userService
from fastapi import HTTPException


def get_use(id: int):
    user = userService.get_user(id)
    return {"use": user["use"]}
 

def get_subjects(id: int):
    user = userService.get_user(id)
    return {"name": user["name"], "subjects": user["subjects"]}

def get_qcm(id: int, nb_questions: int):
    user = userService.get_user(id)
    if not user["use"]:
       raise HTTPException(status_code=400, detail='use is not define')
    if not user["subjects"]:
        raise HTTPException(status_code=400, detail='subjects are empty')
    return qcmService.qcm_builder(id, nb_questions, user)

def login(header):
    if None == header:
        raise HTTPException(status_code=401, detail='wrong credentials')
    header = header.split(" ")[1]
    user = userService.get_user_by_name(header.split(":")[0])
    if user["password"] != header.split(":")[1]:
        raise HTTPException(status_code=401,detail='wrong credentials')
    user["connected"] = True
    return {"conected": user["connected"]}
