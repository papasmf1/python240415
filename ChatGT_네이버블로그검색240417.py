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

for page in range(1, 301):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    #<span class="fds-info-sub-inner-text WNE6DfqawXbjKLCLcd4a">4일 전</span>
    posts = soup.find_all('div', {'class':'fds-ugc-block-mod-list TzMwZlZvvsqG1fk06DNb'})
    for post in posts:
        try:
            #<span class="<span class="m4k_AnOFgU2P631SabRj"><mark>아이폰15</mark> 핑크 자급제 쿠팡 구매후기</span>"><mark>아이폰15</mark> 핑크 자급제 쿠팡 구매후기</span>
            blog_address_elem = post.find("a", 
                attrs={"class":"QS0gep6K3wmBGxMdfuA3 fds-info-inner-text"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("span", attrs={"class":"m4k_AnOFgU2P631SabRj"})
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        

        # <a nocr="1" href="https://in.naver.com/dbgpwls1117/contents/internal/660343443938016?areacode=itb_bas%2Af_other&amp;query=%EC%95%84%EC%9D%B4%ED%8F%B015" class="fwA5zB9fKvQZcIwEGZoQ fds-comps-right-image-text-title" 
        #<span class="fds-info-sub-inner-text m4k_AnOFgU2P631SabRj">2024.02.10.</span>
        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text m4k_AnOFgU2P631SabRj'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find("span", attrs={"class":"m4k_AnOFgU2P631SabRj"})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address, blog_address_title, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)