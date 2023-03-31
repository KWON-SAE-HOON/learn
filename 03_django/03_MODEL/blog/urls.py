# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Create
    # blog/new/
    path('new/', views.new, name='new'),
    # blog/create/ [사용자 입력 데이터]
    path('create/', views.create, name='create'),
        
    # blog/
    path('', views.index, name='index'),
    # blog/2/
    path('<int:article_pk>/', views.detail, name='detail'),   
    
    # Update
    # blog/1/edit/
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    #blog/update/
    path('<int:article_pk>/update/', views.update, name='update'),


    #Delete
    # blog/1/delete
    path('<int:article_pk>/delete', views.delete, name='delete'),
]


