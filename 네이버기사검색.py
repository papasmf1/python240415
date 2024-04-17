import requests
from bs4 import BeautifulSoup

# 크롤링할 페이지의 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 페이지에 접근하여 HTML 가져오기
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 기사 제목을 담을 리스트
article_titles = []

# 기사 제목이 있는 태그들을 찾아서 리스트에 추가
title_tags = soup.find_all("a", class_="news_tit")
for title_tag in title_tags:
    article_titles.append(title_tag.get_text())

# 결과 출력
for title in article_titles:
    print(title)
