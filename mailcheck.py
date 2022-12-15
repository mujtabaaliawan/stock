from django.core.mail import send_mail

send_mail(
    'Market Favourite Company Price Alert',
    'Favourite Company has reached minimum limit,new value is',
    'mujtaba.ali@ignicube.com',
    ['mujtaba381@gmail.com'],
)