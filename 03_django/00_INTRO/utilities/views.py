from django.shortcuts import render
import random
from . import crawling
from . import lotto

# Create your views here.
def get_lotto(request):
    lucky_numbers = lotto.lucky_number()
    context = {
        'lucky_numbers' : lucky_numbers,     
    }
    return render(request, 'utilities/get_lotto.html', context)


def this_week(request):
    this_number = crawling.get_real_lotto()
    context={
        'this_number' : this_number
    }

    return render(request, 'utilities/this_week.html', context)

def check_lotto(request):
    lotto_result = lotto.lotto_result()
    lucky_numbers = lotto.lucky_number()
    this_number = lotto.crawling.get_real_lotto()
    context = {
        'lotto_result' : lotto_result,
        'lucky_numbers' : lucky_numbers,
        'this_number' : this_number,

    }   
    return render(request, 'utilities/check_lotto.html', context)