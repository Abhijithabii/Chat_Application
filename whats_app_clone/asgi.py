"""
ASGI config for whats_app_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

from chat.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whats_app_clone.settings')

application = get_asgi_application()


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
            path('ws/online/', OnlineStatusConsumer.as_asgi()),
            path('ws/notify/', NotificationConsumer.as_asgi()),
        ])
    ),
    "http": get_asgi_application(),
})