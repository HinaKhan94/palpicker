from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/', views.user_profile, name='user_profile'),
    path('register/', views.RegistrationView.as_view(), name='register'),

]
