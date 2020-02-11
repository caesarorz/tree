from django.urls import path


# from .views import login
from .views import login_account, register

app_name = 'accounts'

urlpatterns = [
    path('login/', login_account, name='login'),
    path('register/', register, name='register'),
]