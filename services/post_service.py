from datas.csv_reader_service import datas
from datas.csv_reader_service import lower_snake_case
import services.user_service as userService
import services.qcm_service as qcmService
from fastapi import HTTPException

def post_use(id:int, use:str):
    if not isinstance(use, str):
        raise HTTPException(status_code=400,detail='Bad Type of use')
    user = userService.set_attributes_user(id, "use", use, True)
    return {
        "name": user["name"],
        "use": user["use"]
    }

def post_subjects(id: int, subjects: list):
    if not isinstance(subjects, list):
        raise HTTPException(status_code=400,detail='Bad Type of use')
    user = userService.get_user(id)
    if not user["use"]: 
        raise HTTPException(status_code=400,detail='use is not define')
    for subject in subjects:
        if lower_snake_case(subject) not in datas[user["use"]]:
            raise HTTPException(status_code=400,detail='cannot add subject cause wrong use')  
        if (lower_snake_case(subject) not in user["subjects"]):
                user["subjects"].append(lower_snake_case(subject))
    return {"name": user["name"], "subjects": user["subjects"]}

def admin_post_question(id: int, use: str, subject: str, question):
    user = userService.get_user(id)
    return qcmService.add_question(use, subject, question)