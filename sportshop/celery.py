import os
from celery import Celery

# для совместимости с джанго и что бы не писать app = Celery('tasks', broker='pyamqp://guest@localhost//')
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sportshop.settings')

app = Celery('sportshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() #включает все таски из фаила tasks.py

# Настраиваем новую таску которая делает рассылку каждые 5 мин
# app.conf.beat_schedule = {
#     # Название такски
#     'send-spam-every-1-min':{
#         # Путь до таски
#         'task': 'sport_equipment.tasks.send_email',
#         # Через сколько повторять
#         'schedule': crontab(minute='*/10')
#     },
# }