from django.urls import path, include
from core.views import index, contact


app_name='core'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]