from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('aboutus/', views.AboutView.as_view(), name='aboutus'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/<str:slug>', views.ContactView, name='contact_from_offer'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]