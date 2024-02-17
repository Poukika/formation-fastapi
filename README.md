# School-fastapi

Toutes les requêtes possède les arguments pour un scénario positif
nb: à lancer dans l'ordre pour chaque section (ex: un user demande un qcm en fonction des sujets demandés qui sont reliés au type de qcm).

### Home 

```
curl -X 'GET' \
'http://localhost:8000/' \
-H 'accept: application/json'
```

### API enable

```
curl -X 'GET' \
'http://localhost:8000/it-works' \
-H 'accept: application/json'
```

### POST use pour un user 

```
curl -X 'POST' \
'http://localhost:8000/user/use' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "use": "toto" }'
```

### GET use pour un user

```
curl -X 'GET' \
'http://localhost:8000/user/1/use' \
-H 'accept: application/json'
```

### POST subjects pour un user
```
curl -X 'POST' \
'http://localhost:8000/user/use' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "use": "Test de positionnement" }'
```
```
curl -X 'POST' \
'http://localhost:8000/user/subjects' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "subjects": ["BDD", "Systèmes distribués"]}'
```

### GET subjects pour un user

```
curl -X 'POST' \
'http://localhost:8000/user/use' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "use": "Test de positionnement" }'
```
```
curl -X 'POST' \
'http://localhost:8000/user/subjects' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "subjects": ["BDD", "Systèmes distribués"]}'
```
```
curl -X 'GET' \
'http://localhost:8000/user/1/subjects' \
-H 'accept: application/json'
```

### Génération random de qcm

```
curl -X 'POST' \
'http://localhost:8000/user/use' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "use": "Test de positionnement" }'
```
```
curl -X 'POST' \
'http://localhost:8000/user/subjects' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{ "id": 1, "subjects": ["BDD", "Systèmes distribués"]}'
```
```
curl -X 'GET' \
'http://localhost:8000/user/1/qcm/20' \
-H 'accept: application/json'
```

### Login

```
curl --location 'http://localhost:8000/login' \
--H 'accept: application/json' \
--H 'Authorization: Basic bob:builder'
```

### Données du fichier csv

```
curl -X 'GET' \
'http://localhost:8000/datas' \
-H 'accept: application/json'
```