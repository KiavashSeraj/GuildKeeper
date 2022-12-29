from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('login/', views.loginLoad),
    path('BShome/', views.BShomeLoad),
    path('personal/', view.personalLoad)
]