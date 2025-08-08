from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, CartView, CartRemoveAllView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # new 
    path('about/', AboutPageView.as_view(), name='about'),  # new
    path('contact/', ContactPageView.as_view(), name='contact'),  # new
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('products/create/', ProductCreateView.as_view(), name='form'),  # new
    path('products/created/', ProductCreateView.as_view(), name='created'),  # new 
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    ]