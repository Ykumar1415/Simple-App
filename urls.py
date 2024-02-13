# myapp/urls.py
from django.urls import path
from .views import login, get_csrf_token

urlpatterns = [
    path('login/', login, name='login'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
]
