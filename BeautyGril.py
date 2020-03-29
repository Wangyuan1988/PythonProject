import urllib.request
from bs4 import BeautifulSoup
import requests
import datetime
import re
from multiprocessing import  Pool, cpu_count
from PIL import Image
from pathlib import Path

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
    if id == '0':
        return
    url=f'https://www.meituri.com/a/{id}/'
    req = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'})
    htmlStr=req.content.decode("utf-8")
    soup = BeautifulSoup(htmlStr,"lxml")
    s=soup.title.string
    count=int(s[s.rfind("[")+1:s.rfind("P]_")])
    name = get_model_name(soup)

    pool = Pool(processes=(cpu_count() - 1))

    for i in range(1,count+1):
        pool.apply_async(download_single_pic, args=(id,i,name))
    
    pool.close()
    pool.join()

def download_single_pic(id,i,name):
    urllib.request.urlretrieve( url=f'https://ii.hywly.com/a/1/{id}/{i}.jpg', filename=f'F:\\~Picture\\_temp\\{name}_{id}_{i}.jpg')

def seperatePic(filepath):
    with Image.open(filepath) as img:
        width, height = img.size
    if width<height:
        Path(filepath).rename(filepath.replace('_temp','_height'))
    else:
        Path(filepath).rename(filepath.replace('_temp','_width'))        

if __name__ == "__main__":
    print("Enter/Paste your content. Ctrl-Z to save it.")

    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    
    count=1
    for id in contents:
        print(f' {count}/{len(contents)} ...')
        download_pic(id)
        count+=1

    pathlist = Path(r'F:\~Picture\_temp').glob('**/*.*')
    for path in pathlist:
        seperatePic(str(path))

    input('Enjoy the girls ')