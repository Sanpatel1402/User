from django.urls import path
from .views import dash, log_out


urlpatterns = [
    path('dashboard/', dash, name='dash'),
    path('logout/', log_out, name='logout'),
]