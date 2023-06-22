from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path("", views.index, name="index"),
    path("stores/", views.stores, name="stores"),
    path("login/", views.loginPage, name="login"),
    path('signup/', views.signup, name="signup"),
    path("signupfinal/",views.signupfinal , name="signupfinal"),
    path('logout/', views.logoutPage, name="logout"),
    path("<int:pk>/", views.sellerDetail, name="sellerDetail"),
    path("update-cart/" , views.updatecart, name="updatecart"),
    path("cart/", views.cart, name="cart"),
    path("profile/", views.profile, name="profile"),
    path("action-cart/", views.upcart, name="actionCart"),
    path("close-cart/", views.closecart, name="closeCart"),
    path("checkout/", views.checkout, name="checkout"), 
    path("checkout-backend/", views.checkoutBackend),
    path("api/mpesa/", views.mpesa, name="mpesa")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)