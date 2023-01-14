from django.urls import path

from .import views

urlpatterns = [
    path('reg/', views.registration_view),
    path('', views.Login_View, name='login'),
    path('home/', views.home_view),
    path('contact/', views.contact_view),
    path('services/', views.services_view),
]