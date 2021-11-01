from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_applications, name='get_all_applications'),
    path('new/', views.new_application, name='new_application'),
    path('clients_person-json/<str:client>/', views.get_json_client_person_data, name='clients_person-json'),
    path('client_address-json/<str:client>/', views.get_json_client_address_data, name='client_address-json'),
    path('clients-json/', views.get_json_client_data, name='clients-json'),
    path('routes', views.get_applications_without_drivers, name='applications_wo_dr'),
    path('routes/<int:pk>/', views.get_application_without_driver, name='application_driver'),
    path('routes/update/<int:pk>/', views.get_application_without_driver, name='application_driver_update'),
    path('store/<int:store_id>/', views.get_store, name='store_applications'),
    path('store/<int:store_id>/changestatus/<int:pk_store>/', views.get_application_for_change_status, name='application_change_status'),
    path('<int:pk>/', views.application, name='application'),
    path('<str:manager>/', views.get_my_applications, name='my_applications'),
    path('driver/<int:pk>/', views.get_driver_applications, name='driver_applications'),
]
