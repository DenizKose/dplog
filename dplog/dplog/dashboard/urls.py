from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_admin, name='dashboard'),
    path('newstore/', views.create_store, name='create_store'),
    path('stores/',views.get_stores, name='stores'),
    path('stores/<int:pk>', views.get_store, name='store'),
    path('stores/update/<int:pk>', views.update_store, name='update_store'),
    path('profiles/', views.get_profiles, name='profiles'),
    path('newprofile/', views.create_profile, name='admin_create_profile'),
    path('updateprofile/<int:pk>', views.update_profile, name='admin_update_profile'),
]
