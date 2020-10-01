from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('service/get', views.get_service, name="get_service"),
    path('service/judge', views.get_judge, name="get_judge"),
]
