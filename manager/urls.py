from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('data/get', views.get_result_list, name="get_result_list"),
]
