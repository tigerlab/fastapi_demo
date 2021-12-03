# FastAPI Demo

### The project shows an integration of FastAPI into an existing Django Project

## Running 

### First is to generate static files for uvicorn (you may still need whitenoise):

```pip install -r requirements.txt```
```python manage.py collectstatic --noinput```

Now you can start FastAPI server by:

```uvicorn <site_name>.asgi:<fastapi_app_instance_name> --reload```  or for wsgi : ```uvicorn <site_name>.wsgi:<fastapi_app_instance_name> --reload```,

and start Django server by: 

```uvicorn <site_name>.asgi:<django_app_instance_name> --port 8001 --reload``` or for wsgi:  

```uvicorn <site_name>.wsgi:<django_app_instance_name> --port 8001 --reload```  or when using Django <= 3.1 (with no async support) ```python manage.py runserver 8001```

Then FastAPI’s OpenAPI documentation will be at http://127.0.0.1:8000/docs/ 

and Django’s admin at http://127.0.0.1:8001/admin/.
