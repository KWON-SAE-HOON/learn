
from . import crawling     # crawling.py 를 가져온다
from . import views
import random

real_numbers, bonus_number = crawling.get_real_lotto()

def lucky_number():
    return random.sample(range(1,46), 6)


def lotto_result():

    lucky_numbers = lucky_number()
    

    
    match_count = len(set(lucky_numbers) & set(real_numbers))
    
    if match_count == 6:
        return '1등!'
        
    elif match_count == 5 and bonus_number in lucky_numbers:
        return '2등'
    elif match_count == 5:
        return '3등'
    elif match_count == 4:
        return '4등'
    elif match_count == 3:
        return '5등'
    
    else:
        return '꽝'