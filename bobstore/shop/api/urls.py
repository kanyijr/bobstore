from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes),
    #path("api/action-cart", views.upcart), 
    #path("api/update-cart", views.updatecart)
   
]