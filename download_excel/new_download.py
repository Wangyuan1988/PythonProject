import pandas as pd
from requests import Session
from bs4 import BeautifulSoup
import urllib.request
import selenium.common.exceptions
import os
import urllib.request
import requests
from urllib.parse import urlparse
from multiprocessing.dummy import Pool as ThreadPool 
import logging

s = requests.session()
pool = ThreadPool(8) 
logging.basicConfig(filename=f'download.log',level=logging.INFO, format='[%(levelname)s]%(asctime)s: %(message)s')


def download(normal_url, file_name_prefix):
    try:
        r = s.get(normal_url,verify=False)
        parsed_uri = urlparse(normal_url)
        domain_str=f"{parsed_uri.scheme}://{parsed_uri.netloc}/"
        download_url=f"{domain_str}download.php?file={normal_url.replace(domain_str,'')}"
        soup = BeautifulSoup(r.content).find(id="dl")
        if soup:
            file_name =f'{file_name_prefix} {soup.text}'
            with open(file_name, "wb") as file:
                response = s.get(download_url,verify=False)
                file.write(response.content)
            print(f'{file_name} download finished')
    except Exception as ex:
        logging.exception(f"url is {normal_url}.file name is {file_name_prefix}. details:{ex}")
        pass

def read_excel(sheet_name,xl):
 
    sheet1 = xl.parse(sheet_name) 
    index = sheet1.columns.get_loc("url") 
    r = list(sheet1)
    c = sheet1.iloc[:,index].tolist()
    # print(r)
    # print(c)
    return c

def save_log_to_excel(dict_data):
    df = pd.DataFrame(data=dict_data)
    df.to_excel(f"Excel_List.xlsx")

if __name__ == '__main__':
    p = r"C:\Users\mark ya wang\Desktop\送付用_遼寧科学技術出版社_2019BIBF_ トーハン版権商談リクエスト書籍まとめ_ポプラ社.xlsx"
    url_list=[]
    para_list= []

    xl = pd.ExcelFile(p) 
    for sheet_name in xl.sheet_names:
        url_list_temp = read_excel(sheet_name,xl)
        para_list_temp=[]
        
        url_list_temp =[x for x in url_list_temp if 'https' in str(x)]
        for i,v in enumerate(url_list_temp):
            para_list_temp.append(f'{sheet_name}_{str(i+1)}')
        
        url_list.extend(url_list_temp)
        para_list.extend(para_list_temp)

    dict ={}
    dict["FileName"]=para_list
    dict["URL"]=url_list
    save_log_to_excel(dict)

    # result = pool.starmap(download, zip(url_list, para_list))
    # pool.close() 
    # pool.join() 
    print('Job Done!')






