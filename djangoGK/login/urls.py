from django.urls import path
from . import views
from .views import UserRegisterView

# URLConf
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.loginLoad, name="login"),
    path('logout_user', views.logout_user, name='logout'),
]