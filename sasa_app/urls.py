from django.urls import path
from . import views

app_name = 'sasa_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('consultation/', views.consultation, name="consultation"),
    path('symptomsChecker/', views.symptomsChecker, name="symptomsChecker"),
    path('results/', views.results, name="results"),
    path('show_symptoms/', views.retrieve_symptoms_input, name="show_symptoms"),  
    path('show_appointments/', views.retrieve_appointments, name="show_appointments"),
    path('delete/<int:id>/', views.delete_appointment, name="delete_appointment"),  
    path('edit/<int:appointment_id>/', views.edit_consultation, name="edit_consultation"),  
]

