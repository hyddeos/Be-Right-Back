from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='startpage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/', views.api, name='api'),
    # path('createsu/', views.create_superuser_view, name='createsu'),
    # path('register/', views.register_view, name="register"), # No need for this at this moment

]
