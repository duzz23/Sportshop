#jбязательно это указать что бы celery работало
from .celery import app as celery_app

__all__ = ("celery_app")