import pandas as pd
from requests import Session
from bs4 import BeautifulSoup
import urllib.request
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
import os
import urllib.request
from requests import get

driver=None
def read_excel(excel_path):
    xl = pd.ExcelFile(excel_path) 
    sheet1 = xl.parse("1st (見本依頼)")  
    r = list(sheet1)
    c = sheet1.iloc[:,28].tolist()
    print(r)
    print(c)
# The methods icol(i) and irow(i) are deprecated now. You can use sheet1.iloc[:,i] to get the i-th col and sheet1.iloc[i,:] to get the i-th row.

def download_file(url):
    # driver.get(url)
    driver.execute_script(f"window.open('{url}', 'new_window2')")

    # element = WebDriverWait(driver,15).until(lambda driver:driver.find_element(By.ID,'dl'))
    # print('Job Done')
    # # # button = driver.find_element_by_id('dl')
    # element.click()

def get_webdirver(headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--start-maximized")
    global driver
    # driver = webdriver.Chrome(executable_path=r"dm_alpha/chromedriver_v77.exe",chrome_options=options)
    driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"chromedriver_v77.exe"),chrome_options=options)
    
    url = 'https://33.gigafile.nu/1103-bcb568177ec5d557c4ddd3524eedb4af2'
    driver.get(url)
    # element = WebDriverWait(driver,15).until(lambda driver:driver.find_element(By.ID,'dl'))
    # element.click()

    driver.execute_script(f"window.open('{url}', 'new_window1')")
    # driver.switch_to_window(driver.window_handles[0])

if __name__ == '__main__':
    # str = r"C:\Users\mark ya wang\Desktop\送付用_遼寧科学技術出版社_2019BIBF_ トーハン版権商談リクエスト書籍まとめ_ポプラ社.xlsx"
    # read_excel(str)
  
    url='https://33.gigafile.nu/download.php?file=1103-bcb568177ec5d557c4ddd3524eedb4af2'
    # https://33.gigafile.nu/download.php?file=1103-b86449298c811bb316945b37c1e8da686
    file_name='test.pdf'
    
    get_webdirver()
    download_file(url)


# https://stackoverflow.com/questions/17063458/reading-an-excel-file-in-python-using-pandas
# https://stackoverflow.com/questions/38280094/python-requests-with-multithreading





