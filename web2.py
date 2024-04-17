# web2.py 
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
#페이지 실행 요청
response = requests.get(url)
#검색이 용이한 객체
soup = BeautifulSoup(response.text, "html.parser")

#파일에 저장(매일 크롤링 첨부)
f = open("daangn.txt", "a+", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"} )
    title = titleElem.text.strip()
    priceElem = post.find("div", attrs={"class":"card-price"} )
    price = priceElem.text.strip()
    addrElem = post.find("div", attrs={"class":"card-region-name"} )
    addr = addrElem.text.strip()
    #화면에 출력(format-string): python 3.6 
    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n")
#파일 닫기
f.close() 