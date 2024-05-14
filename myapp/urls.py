from django.urls import path
from .views import analyze_comments

urlpatterns = [
    path('analyze/', analyze_comments, name='analyze_comments'),
]