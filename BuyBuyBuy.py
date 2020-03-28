from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import datetime

options = Options()
ua = UserAgent()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(
    executable_path='C:/Users/Kevin/Desktop/PythonProject/Selenium/chromedriver.exe', chrome_options=options)

def buy(buytime):
  while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if now == buytime:
        try:
          if driver.find_element_by_id("J_Go"):
            driver.find_element_by_id("J_Go").click()
          driver.find_element_by_link_text('提交订单').click()
        except:
          time.sleep(1)
    print(now)

def inputLogin():
    if browser.find_element_by_id('J_Quick2Static'):
        browser.find_element_by_id('J_Quick2Static').click()
    username = browser.find_element_by_id('TPL_username_1')
    password = browser.find_element_by_id('TPL_password_1')
    username.send_keys("王圈圈小公主")
    time.sleep(3)
    password.send_keys("xiaogongzhu520")
    time.sleep(5)
    browser.find_element_by_id('J_SubmitStatic').click()

if __name__ == "__main__":
    browser.get('https://www.taobao.com')
    
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()

    time.sleep(20)
 
    shopcart=browser.find_element_by_id('mc-menu-hd')
    shopcart.click()

    selectAll=browser.find_element_by_id('J_SelectAll1')
    selectAll.click()

    buy=browser.find_element_by_id('J_Go')
    buy.click()

    if browser.find_element_by_link_text('提交订单'):
        browser.find_element_by_link_text('提交订单').click()



