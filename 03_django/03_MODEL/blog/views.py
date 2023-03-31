from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 사용자에게 form이 닮긴 html을 보여줌
def new(request):
    
    return render(request, 'blog/new.html')
   

def create(request):
    # 새로운 게시글(Article instance)를 생성
    article = Article()
    article.title = request.POST['title'] 
    article.content = request.POST['content']
    article.save()

    # 추후 수정 예쩡
    return redirect(f'/blog/{article.pk}')
    # return render(request, 'blog/new.html')
    # 밑에꺼는 주소는 blog/create html은 new.html을 보여줌 redirect가 더 낫다
    # redirect는 /blog/를 다시 써줘야하기 때문에 /로 시작함
# 게시글 목록을 사용자에게 html로 보여줌
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'blog/index.html', context)

# 게시글 상세내용을 html로 보여줌
#        article_pk: var routing 으로 넘어온 값
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)   
    # /article_pk 주소는 int article(pk=article_pk)를 불러옴
    context = {
        'article' : article,
    }
    return render(request,'blog/detail.html', context)


def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'blog/edit.html', context)
# 수정

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST['title'] 
    article.content = request.POST['content']
    article.save()
    
    return redirect(f'/blog/{article.pk}')
    # == return redirect(f'/blog/{article_pk}')
    # 내용 채우고
    # 저장



# 특정 게시글의 삭제 / var routing
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/blog')