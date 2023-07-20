from django.urls import path
from .views import register, reg

urlpatterns = [
    path('', register, name='register'),
    path('reg/', reg, name='reg'),
]
