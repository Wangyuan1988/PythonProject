import urllib.request
from bs4 import BeautifulSoup
import requests
import datetime
import re
import gevent

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
    req = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'})
    htmlStr=req.content.decode("utf-8")
    soup = BeautifulSoup(htmlStr,"lxml")
    s=soup.title.string
    count=int(s[s.rfind("[")+1:s.rfind("P]_")])
    name = get_model_name(soup)
    jobs = [gevent.spawn(urllib.request.urlretrieve, url=f'https://ii.hywly.com/a/1/{id}/{i}.jpg', filename=f'F:\\~Picture\\temp\\{name}_{id}_{i}.jpg') for i in range(1,count+1)] 
    gevent.wait(jobs)


if __name__ == "__main__":
    id = input('id number:')

    while id is not '0':
        download_pic(id)
        id = input('id number:')
