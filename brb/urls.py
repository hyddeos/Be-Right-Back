from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='startpage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('register/', views.register_view, name="register"), # No need for this at this moment
    path('api/', views.api, name='api'),
] 
