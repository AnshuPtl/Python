from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('albums',views.albums,name='albums'),
    path('event',views.event,name='events'),
    path('news',views.news,name='news'),
    path('contact',views.contact,name='contact'),
]
