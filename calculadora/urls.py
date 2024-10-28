from django.urls import path
from calculadora.views import index

urlpatterns = [
    path('', index, name='calculadora')
]