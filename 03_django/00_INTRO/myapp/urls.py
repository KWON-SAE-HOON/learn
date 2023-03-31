# myapp/urls.py

from django.urls import path
# 현재 파일 위치와 같은 위치에
#  views.py 를 import
from . import views


# myapp/hello
urlpatterns = [
    # myapp/hello/
    path('hello/', views.hello),
    # myapp/hye/
    path('bye/', views.bye),

    path('review/' ,views.review),

    path('index/', views.index),
]