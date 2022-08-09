"""
ASGI config for restft project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django import urls

from django.core.asgi import get_asgi_application
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import consumers
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restft.settings')

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    'http':django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
            # [
            #     # url(r'^ws/test-view', consumers.TestConsumer),
            #     urls(r'ws/socket/',consumers.ChatConsumer),
            # ]
        )  
    ),

})
