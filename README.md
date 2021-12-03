# FastAPI Demo

#### The project shows an integration of FastAPI into an existing Django Project


## Running:

- #### Install Requirements:
    ```pip install -r requirements.txt```

- #### Generate static files for uvicorn:

    ```python manage.py collectstatic --noinput```

- #### Start FastAPI server by:

    ```uvicorn fast_api_demo_v2.wsgi:fastapp --reload``` 

- #### Start Django server by: 
    ```python manage.py migrate```

    ```python manage.py runserver 8001```


## Servers:

- FastAPI’s OpenAPI documentation will be at http://127.0.0.1:8000/docs/ 

- Django’s admin at http://127.0.0.1:8001/admin/
