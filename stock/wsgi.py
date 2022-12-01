"""
WSGI config for stock project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock.settings')
# sys.path.append(os.path.dirname(os.path.abspath("C:\Users\Mujtaba Ali\PycharmProjects\scrapyproject1")))

application = get_wsgi_application()
