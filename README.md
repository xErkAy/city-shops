## Getting started

#### Copy the content from .env.example to .env file
```
cp .env.example .env
```

#### Then build containers with the following command

```
docker-compose up -d
```

#### Make and apply all the migrations.

```
python manage.py makemigrations project
python manage.py migrate project
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate api
```

#### Create a superuser to use Django-Admin panel.

```
cd backend/
python manage.py createsuperuser
```

#### Now, you are ready to use the API.
#### Notice: you have to be authenticated to use the API, so use the:
```
http://localhost:8000/auth/registration/
```
#### to create a user.
#### Then use this to authenticate:
```
http://localhost:8000/auth/
```

#### If you want to see the API docs, then use
```
http://localhost:8000/docs/
```
