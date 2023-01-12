from sportshop.celery import app
from .service import send


#Создаю задачи для celery
@app.task # этот декоратор говорит что это Таска
def send_email(user_email):
    send(user_email)




# celery -A sportshop worker -l INFO команда запуска таски



# @app.task # этот декоратор говорит что это Таска
# def send_beat_email():
#     for contacts in ContactSent.objects.all():
#         send_mail(
#             "Вы подписались на рассылку",
#             "это письмо будет приходить каждые 1 минy",
#             "duzz@mail.ru",
#             [contacts.email],
#             fail_silently=False,
#         )
# celery -A src beat --loglevel=INFO запуск новой такски с повторение выполнени первой "beat" заместо "woker"
