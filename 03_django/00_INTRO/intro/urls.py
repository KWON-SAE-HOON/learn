"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

    # 폴더          파일

def hello(request):
    from django.http import HttpResponse
    return HttpResponse('Hello World')

urlpatterns = [
    path('admin/', admin.site.urls),
    # 접두사가, myapp/이면 myapp/qwer.py로 던지겠다
    path('myapp/', include('myapp.urls')),
    # 접두사가, hair/면 hair/urls.py로 던지겠다
    path('hair/', include('hair.urls')),
    path('yourapp/', include('yourapp.urls')),
    path('utilities/', include('utilities.urls')),
]      # ulr 받는거, 함수

# 'asdf/' =hair.views => hello