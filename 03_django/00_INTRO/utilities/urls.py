from django.contrib import admin
from django.urls import path, include
from . import views
    # 폴더          파일



urlpatterns = [
    path('get_lotto/', views.get_lotto),
    path('this_week/', views.this_week),
    path('check_lotto/', views.check_lotto),
]