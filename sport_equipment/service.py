from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Привет',
        'анкета принята',
        'duzz@mail.ru',
        [user_email],
        fail_silently=False,
    )

