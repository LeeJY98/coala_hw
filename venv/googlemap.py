from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://nid.naver.com")

time.sleep(0.5)

id_box = driver.find_element_by_css_selector("input#id")
id_box.send_keys("wldudwldhd")
pw_box = driver.find_element_by_css_selector("input#pw")
pw_box.send_keys("wldud123730")

#4. 검색버튼 누르기 // 검색버튼:
login_button = driver.find_element_by_css_selector("input.btn_global")
login_button.click()