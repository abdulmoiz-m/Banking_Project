from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('overview', views.overview, name="overview"),
    path('transfer', views.transfer, name="transfer")
]
