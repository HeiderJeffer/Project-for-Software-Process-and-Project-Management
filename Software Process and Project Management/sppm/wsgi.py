"""
WSGI config for sppm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sppm.settings")

application = Cling(get_wsgi_application())
