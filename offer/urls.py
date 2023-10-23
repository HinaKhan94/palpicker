from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('aboutus/', views.AboutView.as_view(), name='aboutus'),
    path('contact/', views.AboutView.as_view(), name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]