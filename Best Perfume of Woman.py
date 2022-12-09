import time
import os
#import connectionSetting
#import pymysql
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import subprocess
import shutil

try:
    shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
except FileNotFoundError:
    pass

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
path = "C:\webDriver\chrome\chromedriver_win32\chromedriver.exe"

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

url="https://www.fragrantica.com/awards2021/category/Best-Women-s-Perfume-of-All-Time"
driver.get(url)
"""
elements = driver.find_elements_by_css_selector('.cell small-6 large-4 nomination-box flex-container flex-dir-column align-justify')

for i in range(0, len(elements)):
    # 향수 개별 페이지로 들어가기
    aTag = elements[i].find_element_by_tag_name("a")
    aTag.send_keys(Keys.ENTER)

    # 향수 이름
    el_name = driver.find_element_by_xpath('//*[@id="toptop"]/h1')

    # 향수 브랜드
    el_brand = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[2]/p/a/span')
    
    # 향수 이미지
    images = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/img')
    img_url = []
         
    for image in images :
        url = image.get_attribute('src')
        img_url.append(url)
    
    print(el_name.text)
    print(el_brand.text)
    print(img_url)
#driver.close()
"""
