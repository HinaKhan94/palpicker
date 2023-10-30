from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/', views.user_profile, name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.RegistrationView.as_view(), name='register'),

]
