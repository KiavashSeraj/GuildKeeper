from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('BShome/', views.BShomeLoad),
    path('personal/', views.personalLoad),
]