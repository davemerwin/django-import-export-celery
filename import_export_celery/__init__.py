from django.conf import settings
import importlib

celery_module = settings.CELERY_INIT_MODULE
# from settings.DIEC_NAME import app as celery_app
celery_app = importlib.import_module(celery_module).app