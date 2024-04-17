import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_naver_blog(search_keyword, max_pages=100):
    base_url = "https://search.naver.com/search.naver"
    
    wb = Workbook()
    ws = wb.active
    ws.append(["블로그명", "블로그주소", "제목", "포스팅날짜"])

    for page in range(1, max_pages + 1):
        params = {
            "where": "post",
            "query": search_keyword,
            "start": (page - 1) * 10 + 1
        }

        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')

        blog_posts = soup.find_all("li", class_="bx")

        for post in blog_posts:
            blog_name = post.find("a", class_="sub_txt").get_text()
            blog_url = post.find("a", class_="sub_txt")["href"]
            title = post.find("a", class_="sh_blog_title").get_text()
            post_date = post.find("span", class_="sub_time").get_text()

            ws.append([blog_name, blog_url, title, post_date])

    wb.save("c:\\work\\result.xlsx")

if __name__ == "__main__":
    search_keyword = input("검색어를 입력하세요: ")
    crawl_naver_blog(search_keyword, max_pages=100)
