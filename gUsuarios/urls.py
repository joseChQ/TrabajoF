from django.contrib.auth import views 
from django.urls import path
from .views import Login
from .views import Signup

urlpatterns = [
    path('login/', Login.as_view() , name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('signup/', Signup.as_view(), name = 'signup'),
]