from . import views
from django.urls import path



urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('aboutus/', views.AboutView.as_view(), name='aboutus'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/<str:slug>', views.ContactView.as_view, name='contact_from_offer'),
    path('create_offer/', views.CreateOfferView.as_view(), name='create_offer'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('delete_offer/<int:offer_id>/', views.DeleteOfferView, name='delete_offer'),
    path('edit_offer/<int:post_id>/', views.EditOfferView, name='edit_offer'),
]