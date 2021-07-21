import os

import django
from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') #or .settings
django.setup()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
    "ws": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})