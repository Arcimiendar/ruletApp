from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/rulet/<int:department_id>', consumers.RuletConsumer),
]