from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # new 
    path('about/', AboutPageView.as_view(), name='about'),  # new
    path('contact/', ContactPageView.as_view(), name='contact'),  # new
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create/', ProductCreateView.as_view(), name='form'),  # new 
    ]