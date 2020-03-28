import requests
from bs4 import BeautifulSoup
import queue
import threading

class GetProxies(object):
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.ipQueue =queue.Queue()
        self.work_thread_num = 10
        self.resultList = []
        self.threads=[]

    def get_proxies(self):
        url = 'http://www.xicidaili.com/nt/1'
        html = requests.get(url, headers=self.headers).content
        soup = BeautifulSoup(html, 'xml')
        #tds= soup.find_all('td')[2].text
        # return tds
        tds = soup.find_all('td')
        start = 1
        while start <= len(tds):
            self.ipQueue.put(f"{tds[start].text}:{tds[start+1].text}")
            start += 10

    def verify_one_proxy(self):
        while not self.ipQueue.empty():
            try:
                ip = self.ipQueue.get()
                if requests.get('http://www.bing.com', proxies={'http': ip}, timeout=2).status_code == 200:
                    self.resultList.append(ip)
            except:
                continue
            finally:
                self.ipQueue.task_done()

    def verify_proxy(self):
        for _ in range(self.work_thread_num):
            t = threading.Thread(target=self.verify_one_proxy)
            t.start()
            self.threads.append(t)
            
        self.ipQueue.join()

if __name__ == '__main__':
    a = GetProxies()
    a.get_proxies()
    a.verify_proxy()
    print(len(a.resultList))