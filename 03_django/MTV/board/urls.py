from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name= 'index'),
    # 메인화면
    path('new/', views.new, name='create'),
    # 생성

    path('create/', views.create, name='create'),
    # 크리에이트

    path('<int:notice_pk>/', views.detail, name='detail' ),
    # 조회

    path('<int:notice_pk>/delete/', views.delete, name='delete'),
    # 삭제

    path('<int:notice_pk>/edit/', views.edit, name='edit'),
    # 수정

    path('<int:notice_pk>/update/', views.update, name='update')
]