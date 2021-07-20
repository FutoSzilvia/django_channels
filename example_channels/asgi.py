import os

#from django.core.asgi import get_asgi_application
from channels.layers import get_channel_layer

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example_channels.settings')

#application = get_asgi_application()
channel_layer = get_channel_layer()
