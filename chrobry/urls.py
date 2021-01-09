from django.urls import path
from . import views

app_name = 'chrobry'
urlpatterns = [
    path('', views.index,name="index"),
    path('view',views.view,name="data_view")
]
