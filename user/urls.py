from django.urls import path
from .views import user, about, contact

urlpatterns = [
    path('', user, name='user'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
