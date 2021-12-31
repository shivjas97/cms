from django.urls import path
from. import views


urlpatterns = [

    path('',views.index, name='index'),
    path('hrlogin',views.hrlogin, name='hrlogin'),
    path('clintlogin',views.clintlogin, name='clintlogin'),
    path('adminlogin',views.adminlogin, name='adminlogin'),
    path('managerlogin',views.managerlogin, name='managerlogin'),
    path('devloperlogin',views.devloperlogin, name='devloperlogin'),

 ]