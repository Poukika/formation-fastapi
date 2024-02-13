import services.user_service as userService

def delete_subjects(id: int):
    user = userService.get_user(id)
    user["subejcts"] = [] 
    return {"name": user["name"], "subjects": user["subjects"]}