import urllib.request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import datetime
import re

ua = UserAgent()

def get_model_name(soup):
    div=soup.find("div",{"class":"tuji"})
    name=None
    p=None
    for item in div.find_all("p"):
        if '出镜模特' in item.text:
            p=item
            break
    if p:
        a = p.find_all('a')
        if len(a)>0:
            name = a[0].text
        else:
            name= p.text.replace('\n','').strip().lstrip('出镜模特：')
    return name 

def download_pic(id):
    if id is '0':
        return
    url=f'https://www.meituri.com/a/{id}/'
    # url=url.rstrip("/")
    # id=url[url.rfind("/")+1:]
    req = requests.get(url, headers={'User-Agent': ua.random})
    htmlStr=req.content.decode("utf-8")
    soup = BeautifulSoup(htmlStr,"lxml")
    s=soup.title.string
    count=int(s[s.rfind("[")+1:s.rfind("P]_")])
    name = get_model_name(soup)
    for i in range(1,count+1):
        urllib.request.urlretrieve(url=f'https://ii.hywly.com/a/1/{id}/{i}.jpg', filename=f'F:\\~West\\{name}_{datetime.datetime.now().strftime("%Y%m%d")}_{id}_{i}.jpg')
        
if __name__ == "__main__":
    id = input('id number:')

    while id is not '0':
        download_pic(id)
        id = input('id number:')
