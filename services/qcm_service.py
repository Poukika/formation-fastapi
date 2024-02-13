from datas.csv_reader_service import datas
from random import sample
from datas.csv_reader_service import lower_snake_case
from fastapi import HTTPException
import copy

def qcm_builder(id: int, nb_questions: int, user: dict):
    questions_by_user = get_datas_from_user(user)
    questions_by_user = sample(questions_by_user, k=nb_questions if nb_questions < len(questions_by_user) else len(questions_by_user))
    for index, question in enumerate(questions_by_user):
        if question["answer"] == "":
            questions_by_user.pop(index)
    return questions_by_user


def get_datas_from_user(user: dict):
    questions_by_user = []
    for subject in user["subjects"]:
        questions_by_user = questions_by_user + datas[user["use"]][subject]

    return questions_by_user

def add_question(use:str, subject:str, question):
    use = lower_snake_case(use)
    subject = lower_snake_case(subject)
    if use not in datas[use]:
        raise HTTPException(status_code=400,detail="use doesn't exist")
    if subject not in datas[use][subject]:
        raise HTTPException(status_code=400,detail='No subject with this type')
    datas[use][use].append(vars(question))
    return datas[use][subject]
