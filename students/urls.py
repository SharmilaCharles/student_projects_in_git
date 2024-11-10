from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.StuApp_detail, name='StuApp_detail'),  
    
]
