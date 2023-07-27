"""
WSGI config for oficina_virtual project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import threading
from django.core.wsgi import get_wsgi_application
from oficina_virtual_app.sync_airtable import sync_airtable

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

threading.Thread(target=sync_airtable).start()
