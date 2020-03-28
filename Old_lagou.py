'''
Function:
	爬取拉勾网招聘数据
作者:
	Charles
公众号:
	Charles的皮卡丘
'''
import os
import re
import time
import pickle
import urllib
import random
import requests
import sys

#https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false
headers = {
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
			'Connection': 'keep-alive',
			'Content-Length': '19',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Host': 'www.lagou.com',
			'Origin': 'https://www.lagou.com',
			'X-Anit-Forge-Code': '0',
			'X-Anit-Forge-Token': 'None',
			'X-Requested-With': 'XMLHttpRequest',
			'Cookie':'JSESSIONID=ABAAABAAAIAACBI81F5B6390151C54A14C4CE570466952F; _ga=GA1.2.1818024885.1547975979; _gid=GA1.2.503967608.1547975979; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547975980; user_trace_token=20190120171938-82cdac39-1c94-11e9-8322-525400f775ce; LGSID=20190120171938-82cdad2c-1c94-11e9-8322-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190120171938-82cdae8a-1c94-11e9-8322-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; _gat=1; LGRID=20190120172145-ce59d737-1c94-11e9-8322-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547976107; SEARCH_ID=d422ff6b6c9d46b9a9250ea6f25c8aea'
			}


# 定义爬虫
def Crawler(savefile='info.pkl'):
	url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city={}&needAddtionalResult=false'
	infoDict = {}
	for city in ['上海', '北京', '广州', '南京', '深圳', '杭州', '成都', '武汉', '天津']:
		infoDict[city] = []
		city_quote = urllib.parse.quote(city)
		headers['Referer'] = 'https://www.lagou.com/jobs/list_?px=new&city=%s' % city_quote
		url_now = url.format(city_quote)
		for page in range(1, 31):
			print('[INFO]: Get <%s>-<Page.%s>' % (city, page))
			data = 'first=true&pn={}&kd=python'.format(page)
			try:
				res = requests.post(url_now, data=data.encode('utf-8'), headers=headers)
				res_json = res.json()['content']['positionResult']['result']
			except:
				type,value,traceback=sys.exc_info()
				print(value)
				
				break
			for rj in res_json:
				infoDict[city].append([rj.get('companyFullName', '无'), 
									   rj.get('companyShortName', '无'), 
									   rj.get('positionName', '无'), 
									   rj.get('positionAdvantage', '无'), 
									   rj.get('industryField', '无'), 
									   rj.get('companySize', '无'), 
									   rj.get('jobNature', '无'), 
									   rj.get('education', '无'), 
									   rj.get('workYear', '无'), 
									   rj.get('salary', '无')])
			time.sleep(random.randint(40, 60))
	f = open(savefile, 'wb')
	pickle.dump(infoDict, f)



if __name__ == '__main__':
	Crawler()