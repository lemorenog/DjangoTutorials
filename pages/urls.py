from django.urls import path

from pages.utils import ImageLocalStorage
from .views import HomePageView, AboutPageView, ContactPageView, ImageViewFactory, ImageViewNoDI, ProductIndexView, ProductShowView, ProductCreateView, CartView, CartRemoveAllView

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
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'), 
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'), 
    path('image/save', ImageViewNoDI.as_view(), name='imagenodi_save'),
    ]