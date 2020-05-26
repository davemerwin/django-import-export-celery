from django.conf import settings
import importlib

celery_module = getattr(settings, 'IMPORT_EXPORT_CELERY_INIT_MODULE', 'project.celery')
# from settings.DIEC_NAME import app as celery_app
celery_app = importlib.import_module(celery_module).app