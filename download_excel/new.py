import pandas as pd
from requests import Session
from bs4 import BeautifulSoup
import urllib.request
import selenium.common.exceptions
import os
import urllib.request
import requests

s = requests.session()


def download(normal_url, file_name_prefix):
    r = s.get(normal_url,verify=False)
    download_url='https://33.gigafile.nu/download.php?file='+normal_url.replace('https://33.gigafile.nu/','')
    soup = BeautifulSoup(r.content)
    file_name =f'{file_name_prefix} {soup.find(id="dl").text}'

    with open(file_name, "wb") as file:
        response = s.get(download_url,verify=False)
        file.write(response.content)
    print(f'{file_name} download finished')

def read_excel(excel_path):
    xl = pd.ExcelFile(excel_path) 
    sheet1 = xl.parse("1st (見本依頼)")  
    r = list(sheet1)
    c = sheet1.iloc[:,28].tolist()
    print(r)
    print(c)
    return c

if __name__ == '__main__':
    # url = 'https://33.gigafile.nu/1103-bcb568177ec5d557c4ddd3524eedb4af2'
    # url='https://33.gigafile.nu/download.php?file=1103-bcb568177ec5d557c4ddd3524eedb4af2'

    # https://33.gigafile.nu/download.php?file=1103-b86449298c811bb316945b37c1e8da686

    p = r"C:\Users\mark ya wang\Desktop\送付用_遼寧科学技術出版社_2019BIBF_ トーハン版権商談リクエスト書籍まとめ_ポプラ社.xlsx"
    url_list = read_excel(p)
    index=1
    for item in [x for x in url_list if 'https' in str(x)]:
        download(item,str(index))
        index+=1

    # download('https://33.gigafile.nu/1103-bcb568177ec5d557c4ddd3524eedb4af2','https://33.gigafile.nu/download.php?file=1103-bcb568177ec5d557c4ddd3524eedb4af2','test')





