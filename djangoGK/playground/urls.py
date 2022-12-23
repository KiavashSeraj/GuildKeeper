from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('title/', views.titleLoad),
    path('homepage/', views.homeload)
]