import time
from selenium import webdriver
from time import strftime
from selenium.webdriver.common.keys import Keys

PATH = "E:\\Projects\\aida\\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://web.whatsapp.com/")

print('Please Enter The QR-Code')
time.sleep(10)
print('sub')
contact = "The little moon"

search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)

txt = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
while True:
    msg = "I Love U"
    txt.send_keys(msg)
    txt.send_keys(Keys.ENTER)
    time.sleep(180)
