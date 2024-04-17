# web1.py 
from bs4 import BeautifulSoup

#파일 로딩(함수체인, 메서드체인)
page = open("Chap09_test.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")
#전체 보기 
#print( soup.prettify() )
#<p>태그 전체 검색: ResultSet리턴 -> List 비슷한 파생형식 
#print( soup.find_all("p") )
#<p> 하나를 검색 
#print( soup.find("p") )
#<p class='outer-text'> 조건 검색 
#print( soup.find_all("p", class_ = "outer-text") )
#조건: attrs 속성명 dict형식으로 나열 
#print( soup.find_all("p", attrs={"class":"outer-text"}))

#id속성 검색 
#print( soup.find_all(id="first"))

#태그 내부에 문자열: .text, get_text() 
for tag in soup.find_all("p"):
    #내부 문자열 리턴 
    title = tag.text.strip()
    #줄바꿈 문자 변환
    title = title.replace("\n", "")
    print(title)



