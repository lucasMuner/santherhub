"""
WSGI config for gerenciamento_de_funcionarios project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from gerenciamento_de_funcionarios.settings import base
from django.core.wsgi import get_wsgi_application

if base.DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gerenciamento_de_funcionarios.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'gerenciamento_de_funcionarios.settings.production')


application = get_wsgi_application()
