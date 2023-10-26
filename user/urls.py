from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('user_profile/', views.profile, name='user_profile'),

]
