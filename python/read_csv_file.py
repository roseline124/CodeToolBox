"""
연습문제 11-8 CSV 파일 읽어들이기

스프레드시트 또는 텍스트 편집기를 이용해 
다음 표의 내용을 CSV 파일로 작성해라.

이 CSV 파일을 읽어들이고 각 나라의 인구밀도를 구해 
인구밀도가 높은 나라부터 낮은 나라 순으로 나라 이름과 
인구밀도를 출력하는 프로그램을 작성해라.

인구밀도 = 인구(명)/전체 면적(km**2)
"""

import csv
from pprint import pprint

with open('population_density.csv', 'r', encoding='utf-8') as f : 

    data = csv.reader(f)
    country = list(data)[1:] #header 제외
    rank = 0
    _dict = {}

    for c in country : 
        name, population, area = c
        density = round(int(population)/int(area)) 
        _dict[name] = density 

    ordered_countries = sorted(_dict, reverse=True, key=lambda n : _dict[n])
    form = '{0}위: {1:15} | 인구 밀도 : {2:10}'

    for c in ordered_countries :
        rank += 1
        print(form.format(rank, c, _dict[c]))

