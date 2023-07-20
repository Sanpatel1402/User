from django.urls import path
from .views import signin, log

urlpatterns = [
    path('', signin, name='login'),
    path('log/', log, name='log'),
]
