from django.shortcuts import render, redirect
from .models import Student
from . forms import StudentForm

# def new(request):
#     form =StudentForm()
#     return render(request, 'blog/new.html',{
#         'form' : form,
#     })
                
# def create(request):
#     # form 에 사용자 입력 데이터 붙임
#     form = StudentForm(request.POST)
#     # form이 유효하면 세이브
#     if form.is_valid():
#         form.save()
#         return redirect('/blog/')  
#     else:   # 아닐 시 뒤로 돌아감
#         return render(request, 'blog/new.html',{
#             'form':form
#         })
    
def create(request):
    if request.method == 'GET':   # 이전의 /blog/new/
        form = StudentForm()
        return render(request, 'blog/new.html', {
            'form': form,
        })

    elif request.method == 'POST':  #이전의 /blog/create
        form = StudentForm(request.POST)
        # data가 유효하다면,
        if form.is_valid():
            form.save()
            return redirect('/blog/new/')
        # data가 유효하지 않다면
        else:
            return render(request, 'blog/new.html', {
                'form': form
            })


def index(request):
    students = Student.objects.order_by('-balance')
    context = {
        'students' : students,
    }
    return render(request, 'blog/index.html', context)

def detail(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    return render(request, 'blog/detail.html', {
        'student': student,
    })


def edit(request, student_pk):
    
    return render(request, 'blog/edit.html')

def update(request, student_pk):

    return redirect('')

def delete(request, student_pk):

    student = Student.objects.get(pk=student_pk)
    student.delete()
    return redirect('/blog/')