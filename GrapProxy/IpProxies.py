import requests
from bs4 import BeautifulSoup
import queue
import threading
from multiprocessing.dummy import Pool as ThreadPool
from pymongo import MongoClient
import datetime


class GetProxies(object):
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.ipList =[]
        self.work_thread_num = 10
        self.resultList =[]
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.Scrapy
        self.collection = self.db.IpProxy

    def get_proxies(self,index):
        url = f'http://www.xicidaili.com/nt/{index}'
        html = requests.get(url, headers=self.headers).content
        soup = BeautifulSoup(html, 'xml')
        #tds= soup.find_all('td')[2].text
        # return tds
        tds = soup.find_all('td')
        start = 1
        while start <= len(tds):
            self.ipList.append(f"{tds[start].text}:{tds[start+1].text}")
            start += 10

    def verify_one_proxy(self, ip):
        # for ip in self.ipList:
        #     try:
        #         if requests.get('http://www.bing.com',proxies={'http':ip},timeout=2).status_code !=200:
        #             self.ipList.remove(ip)
        #     except:
        #         self.ipList.remove(ip)

        try:
            if requests.get('http://www.lagou.com', proxies={'http': ip}, timeout=2).status_code == 200:
                self.resultList.append({'ip':ip.split(':')[0],'port':ip.split(':')[1],'verifyDate':datetime.datetime.now()})
        except:
            pass

    def verify_proxy(self):
        pool = ThreadPool(self.work_thread_num)
        pool.map(self.verify_one_proxy, self.ipList)
        pool.close()
        pool.join()
        return

    def storeIp(self):
        if len(self.resultList) is not 0:
            for item in self.resultList:
                self.collection.replace_one({'ip':item['ip']},item,upsert=True)
            self.resultList.clear()

if __name__ == '__main__':
    a = GetProxies()
    count=int(input('count:'))
    for i in range(1,count):
        a.get_proxies(i)
        a.verify_proxy()
        print(len(a.resultList))
        a.storeIp()