from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]

