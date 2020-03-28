import json
import requests
import time
import urllib.parse
import lagouconfig
from fake_useragent import UserAgent
from pymongo import MongoClient
import pysnooper


@pysnooper.snoop()
def get_json(url, datas, kd, city):
    ua = UserAgent()
    my_headers = {
        "User-Agent":ua.random,
        "Referer": f"https://www.lagou.com/jobs/list_{kd}?city={city}&cl=false&fromSearch=true&labelWords=&suginput=",
        "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
    }
    time.sleep(5)
    ses = requests.session()    # 获取session
    ses.headers.update(my_headers)  # 更新
 
    proxyDict = { 
                    "http"  : "http://203.191.145.167:8080"
                }

    ses.get(
        f"https://www.lagou.com/jobs/list_{kd}?city={city}&cl=false&fromSearch=true&labelWords=&suginput=",proxies=proxyDict)

    content = ses.post(url=url, data=datas,proxies=proxyDict)
    result = content.json()
    return result['content']['positionResult']['result']


def insert_mongodb(data):
    jobcollection = MongoClient('mongodb://localhost:27017/').Job.LagouNew
    for item in data:
        jobcollection.replace_one(
            {'positionId': item["positionId"]}, item, True)


def main():
    page = lagouconfig.pagesize
    kd = urllib.parse.quote_plus(lagouconfig.kd)
    city = urllib.parse.quote_plus(lagouconfig.city)

    for x in range(1, page+1):
        url = f'https://www.lagou.com/jobs/positionAjax.json?city={city}&needAddtionalResult=false'
        datas = {
            'first': 'false',
            'pn': x,
            'kd': kd,
        }
        try:
            info = get_json(url, datas, kd, city)
            insert_mongodb(info)
            print(f"Page {x} finished..")
        except Exception as msg:
            print(f"Page {x} error,message：{msg}")


if __name__ == '__main__':
    main()
