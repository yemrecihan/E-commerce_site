from django.urls import path
from .import views
app_name='ToyShopapp'

urlpatterns = [
    
    path('', views.toy_list, name= 'home'),
    path('toylist/', views.toy_list, name= 'toy_list'),
    path('toydetail/<int:toy_id>/', views.toy_detail, name= 'toy_detail'),
    path('addToCart/<int:toy_id>/',views.add_to_cart,name='addToCart'),
    path('cart/',views.cart,name='cart'),
    path ('checkout/',views.checkout,name='checkout'),
    path('remove_from_cart/<int:toy_id>/', views.remove_from_cart, name='remove_from_cart'),
   
]