from django.urls import path
from .views import chatbot_response,chatbot_view

urlpatterns = [
     path('', chatbot_view, name='chatbot_home'),
    path('get-response/', chatbot_response, name='chatbot_response'),
]
