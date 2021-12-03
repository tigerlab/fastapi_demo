"""
WSGI config for fast_api_demo_v3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fast_api_demo_v3.settings')

application = get_wsgi_application()




# from policies.routers import router as contracts_router
from policies.api.routers import router as contracts_router

fastapp = FastAPI()
fastapp.include_router(contracts_router, tags=["contracts"], prefix="/contract")
