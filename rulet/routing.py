from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from ruletApp.routing import websocket_urlpatterns as rulet_urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
              rulet_urlpatterns
        )
    ),
})
