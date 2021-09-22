# 인스타그램 본문 수집하기

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com")


time.sleep(1)

#로그인 절차
id_box = driver.find_element_by_css_selector("div.rgFsT > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")
id_box.send_keys("lee_jiyeong_xx")
pw_box = driver.find_element_by_css_selector("div.rgFsT > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input")
pw_box.send_keys("wldudtop")

login_box = driver.find_element_by_css_selector("div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button")
login_box.click()

time.sleep(1)

# 알립설정 끄기
notify_box = driver.find_element_by_css_selector("button.aOOlW.HoLwm")
notify_box.click()
driver.get("https://www.instagram.com/explore/tags/ootd/")

#로그린 정보 저장
loginsave = driver.find_element_by_css_selector("button.sqdOP.L3NKy")
loginsave.click()

driver.get("https://www.instagram.com/explore/tags/ootd/")

# 컨테이너
container = driver.find_elements_by_css_selector("div.v1Nh3")
container = container[:12]


for con in container:

    con.click()

    time.sleep(1)

    insta = driver.find_element_by_css_selector("div.C4VMK>span").text
    print(insta)

    close_box = driver.find_element_by_css_selector("button.ckWGn")
    close_box.click()