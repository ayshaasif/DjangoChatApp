from django import urls
from django.urls import re_path
from django.conf.urls import include, url

from . import consumers
# 
websocket_urlpatterns = [
    re_path(r'ws/socket-server',consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/socket-server/<str:chatUuid>',consumers.ChatConsumer.as_asgi()),
    # url(r'^ws/socket-server/(?P<string>[\w\-]+)/$',consumers.ChatConsumer.as_asgi())
]
