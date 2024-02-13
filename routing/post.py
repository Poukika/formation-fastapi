from fastapi import APIRouter, HTTPException
import services.post_service as postService
from pydantic import BaseModel
from typing import List, Union

router = APIRouter()
################ MODELS #################
class UserUse(BaseModel):
    id: int
    use: str

class UserSubjects(BaseModel):
    id: int
    subjects: List[str]

class Content(BaseModel):
    question_text: str
    answer: str
    answer_text: List[str]
    remark: str

class Question(BaseModel):
    id: int
    subject: str
    use: str
    content: Union[Content, None]

###########################################

@router.post('/user/use', tags=['user'])
async def post_use(user_use: UserUse)-> dict:
    """Enregistrement d'un type de qcm par un user
    """
    return postService.post_use(user_use.id, user_use.use)
    

@router.post('/user/subjects', tags=['user'])
async def post_subjects(user_subjects: UserSubjects):
    """Enregistrement des sujets par un user
    """
    return postService.post_subjects(user_subjects.id, user_subjects.subjects)

@router.post('/admin/question', tags=['admin'])
async def admin_post_question(question: Question)-> dict:
    """Ajout d'une question par un admin
    """
    return postService.admin_post_question(question.id, question.use, question.subject, question.content)