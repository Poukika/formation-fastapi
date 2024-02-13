from fastapi import FastAPI
from routing import post, get, delete

app = FastAPI(
    title="FastAPI Exercice",
    description="FastAPI Exercice",
    version="1.1",
    openapi_tags=[
    {
        'name': 'home',
        'description': 'default functions'
    },
    {
        'name': 'admin',
        'description': 'Fonctions admin'
    },
    {
        'name': 'user',
        'description': 'Fonctions User'
    },
    {
        'name': 'autre',
        'description': 'Fonctions utiles'
    }
])

app.include_router(post.router)
app.include_router(get.router)
app.include_router(delete.router)