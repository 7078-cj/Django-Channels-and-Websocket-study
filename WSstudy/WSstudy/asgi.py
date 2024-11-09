"""
ASGI config for WSstudy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter,URLRouter #add this
from chat.routing import wsPattern #add this

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WSstudy.settings')

http_response_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http":http_response_app,
    "websocket":URLRouter(wsPattern)
})