from django.shortcuts import render

from django.http import HttpResponse
import random

# view => function

def bye(request):
    return HttpResponse('Goodbye My Friend')

def hello(request):
    lucky_numbers = random.sample(range(1,46), 6)
    return HttpResponse(' '.join(map(str,(lucky_numbers))))


def review(request):
    return render(request, 'review.html',)

def index(request):
    lucky_numbers = random.sample(range(1,46), 6)
    draw_no = 1078

    context = {
        'lucky_numbers' : lucky_numbers,
        'asdfasdf' : draw_no,

    }

    return render(request, 'myapp/index.html', context)