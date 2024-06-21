from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('stock/add', views.add_stock, name="add_stock"),
    path('stock/delete/<int:pk>', views.delete, name="delete_stock"),
]
