from django.urls import path
from. import views


urlpatterns = [

    path('',views.index, name='index'),

    path('allclint',views.allclint, name='allclint'),
    path('viewclint',views.viewclint, name='viewclint'),
    path('editclint',views.editclint, name='editclint'),
    path('deleteclint',views.deleteclint, name='deleteclint'),

    path('allmanagers',views.allmanagers, name='allmanagers'),
    path('managemanager',views.managemanager, name='managemanager'),
    path('viewmanager',views.viewmanager, name='viewmanager'),
    path('edit',views.edit, name='edit'),
    path('delete',views.delete, name='delete'),

    path('addhr',views.addhr, name='addhr'),
    path('allhr',views.allhr, name='allhr'),
    path('edithr',views.edithr, name='edithr'),
    path('deletehr',views.deletehr, name='deletehr'),
    path('viewhr',views.viewhr, name='viewhr'),

    
    path('addproject',views.addproject, name='addproject'),
    path('allproject',views.allproject, name='allproject'),
    path('editproject',views.editproject, name='editproject'),
    path('viewproject',views.viewproject, name='Viewproject'),
    path('deleteproject',views.deleteproject, name='deleteproject'),

    path('alldevloper',views.alldevloper, name='alldevloper'),
    path('viewdevloper',views.viewdevloper, name='viewdevloper'),
    path('editdevloper',views.editdevloper, name='editdevloper'),
    path('deletedevloper',views.deletedevloper, name='deletedevloper'),

    path('assignproject',views.assignproject, name='assignproject'),
    #path('allhr',views.allhr, name='allhr'),
    
 ]