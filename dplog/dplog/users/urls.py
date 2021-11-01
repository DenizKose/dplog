from django.urls import path

from . import views

urlpatterns = [
    path('<str:profile_name>/', views.profile, name='profile'),
]
