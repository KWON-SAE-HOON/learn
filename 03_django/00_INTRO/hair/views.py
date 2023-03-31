from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def nice(request):
    # render의 첫번째 인자 => request 고정
    # 두번째 인자 템플릿 이름 str
    # 세번째 인자 
    return render(request, 'qwer.html',)


# http://127.0.0.1:8000/hair/nice/