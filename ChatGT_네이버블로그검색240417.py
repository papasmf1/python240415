import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 100):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    posts = soup.find_all('div', {'class':'fds-ugc-block-mod-list TzMwZlZvvsqG1fk06DNb'})
    for post in posts:
        try:
            #<a nocr="1" href="https://in.naver.com/" class="fwA5zB9fKvQZcIwEGZoQ fds-info-inner-text" target="_blank"><span class="m4k_AnOFgU2P631SabRj">혜진</span></a>
            #<span class="<span class="m4k_AnOFgU2P631SabRj"><mark>아이폰15</mark> 핑크 자급제 쿠팡 구매후기</span>"><mark>아이폰15</mark> 핑크 자급제 쿠팡 구매후기</span>
            blog_address_elem = post.find("a", 
                attrs={"class":"fwA5zB9fKvQZcIwEGZoQ fds-info-inner-text"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("span", attrs={"class":"m4k_AnOFgU2P631SabRj"})
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        
        #<span class="fds-info-sub-inner-text WNE6DfqawXbjKLCLcd4a">4일 전</span>
        #<a nocr="1" href="https://blo" class="fwA5zB9fKvQZcIwEGZoQ fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000035493126.90000003_000000000000003403434C3B'" data-cb-trigger="true"><span class="m4k_AnOFgU2P631SabRj"><mark>아이폰15</mark> 색상 순위 고민 구입 꿀팁!</span></a>
        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text m4k_AnOFgU2P631SabRj'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find("a", attrs={"class":"fwA5zB9fKvQZcIwEGZoQ fds-comps-right-image-text-title"})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address_title, blog_address, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)