# crawling.py
# $ pip install requests
# $ pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def get_real_lotto():

    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A1%9C%EB%98%90'

    res = requests.get(url)

    # 요청은 클라이언트 프로그램을 통해 URL로 보낸다

    data = BeautifulSoup(res.text, 'html.parser')

    real_numbers = []

    for tag in data.select('.ball'):            # .ball이 있는 데이터만 골라서 list에 추가
        real_numbers.append(tag.text)


    real_numbers = list(map(int, real_numbers))     # int로 맵핑함

    bonus_numbers = real_numbers.pop()

    # list(map(lambda tag:int(tag.text),data.select('.ball')))
    
    # 보너스 넘버는 pop으로 real_numbers로 remove하고 remove한걸 return
    
    # return {'real_numbers': real_numbers, 'bonus_number': bonus_numbers}
    return real_numbers, bonus_numbers
