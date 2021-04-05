from django.conf.urls import url

from .consumers import ChatConsumer, AsyncChatConsumer, BaseSyncConsumer, BaseAsyncConsumer

websocket_urls = [
    url(r'^ws/chat/$', BaseAsyncConsumer.as_asgi()),
]