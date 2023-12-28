from django.urls import path
from .import views

app_name='foodapp'

urlpatterns=[
    path('',views.index,name='index'),
    path('food/<int:food_id>/', views.detail, name='detail'),

]