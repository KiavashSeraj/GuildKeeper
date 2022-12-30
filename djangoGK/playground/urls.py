from django.urls import path
from . import views
from .views import UserRegisterView

# URLConf
urlpatterns = [
    path('BShome/', views.BShomeLoad),
    path('personal/', views.personalLoad),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', views.loginLoad),
]