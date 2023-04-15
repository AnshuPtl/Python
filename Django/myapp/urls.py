from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about',views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('products',views.products, name='products'),
    path('feedback',views.feedback, name="feedback"),
    path('Signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('user',views.user,name="user"),
]
