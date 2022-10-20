
from django.urls import path, include
from .import views

urlpatterns = [
    path('<int:pk>/<int:page>/', views.main, name='main'),
]
