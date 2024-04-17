from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

#크롬드라이버 실행
driver = webdriver.Chrome() 

#URL주소
driver.get("https://www.google.co.kr")
#3초 대기 
time.sleep(3)

#searchBox = driver.find_element(By.CLASS_NAME, "gLFyf")
#id로 검색 
searchBox = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
searchBox.send_keys("맥북")
searchBox.send_keys(Keys.ENTER)
time.sleep(10)

#<textarea class="gLFyf" aria-controls="Alh6id" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwjihJyJzciFAxX5Z_UHHUFFALcQ39UDCAY" aria-activedescendant="" style=""></textarea>

# while True:
#     pass 