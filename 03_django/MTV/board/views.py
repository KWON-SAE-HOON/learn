from django.shortcuts import render, redirect
from .models import Notice


def index(request):
    notices = Notice.objects.order_by('-rank')      #rank 컬럼 내린차순 정렬
    context = {
        'notices' : notices,
    }
    return render(request, 'board/index.html', context) 

def new(request):
    return render(request, 'board/new.html')

def create(request):
    notice = Notice()
    notice.title = request.POST['title']
    notice.rank = request.POST['rank']
    notice.content = request.POST['content']
    notice.save()
    return redirect('/board')

def detail(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    context = {
        'notice' : notice
    }
    return render(request, 'board/detail.html', context)

def delete(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    notice.delete()
    return redirect('/board')

def edit(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    context = {
        'notice' : notice
    }
    return render(request, 'board/edit.html', context)

def update(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    notice.title = request.POST['title']
    notice.rank = request.POST['rank']
    notice.content = request.POST['content']
    notice.save()
    return redirect(f'/board/{notice_pk}')
