from django.urls import path
from. import views


urlpatterns = [

    path('',views.index, name='index'),

    path('addemployee',views.addemployee,name='addemployee'),
    path('viewdevloper',views.viewdevloper,name='viewdevloper'),
    path('devloperprofile',views.devloperprofile,name='devloperprofile'),
    path('editdevloper',views.editdevloper,name='editdevloper'),
    path('deletedevloper',views.deletedevloper,name='deletedevloper'),
    
    path('addclint',views.addclint,name='addclint'),
    path('viewclints',views.viewclints,name='viewclints'),
    path('clintprofile',views.clintprofile,name='clintprofile'),
    path('editclint',views.editclint,name='editclint'),
    path('deleteclint',views.deleteclint,name='deleteclint'),


    path('addmanager',views.addmanager,name='addmanager'),
    path('managerprofile',views.managerprofile,name='managerprofile'),
    path('viewmanager',views.viewmanager,name='viewmanager'),
    path('editmanager',views.editmanager,name='editmanager'),
    path('deletemanager',views.deletemanager,name='deletemanager'),

 ]
