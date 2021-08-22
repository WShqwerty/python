from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

sleep(2)

driver.quit()