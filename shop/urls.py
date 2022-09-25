from django.urls import path
from . import views

urlpatterns = [
    path('', views.pro, name='product'),
    path('<slug:c_slug>/', views.pro, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.prod_view, name='details'), 
    path('search',views.searching,name='search'), 
    
]
