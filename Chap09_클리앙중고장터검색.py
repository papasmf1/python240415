#Chap09_클리앙중고장터검색.py
# coding:utf-8
#정적인 웹사이트 
from bs4 import BeautifulSoup
#파이썬 내장 Lib
import urllib.request
#정규표현식
import re 

#파일 저장
f = open("clien.txt", "wt", encoding="utf-8")
for n in range(0,10):
        #클리앙의 중고장터 주소 
        url ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(url)
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text" title="아이패드 프로 12.9인치 4세대 256 wifi 스페이스 그레이">
        # 						아이패드 프로 12.9인치 4세대 256 wifi 스페이스 그레이
        # 					</span>
        for item in list:
            title = item.text.strip()
            #키워드 검색
            if re.search("아이패드", title):
                print(title)
                f.write(f"{title}\n")

f.close()  

