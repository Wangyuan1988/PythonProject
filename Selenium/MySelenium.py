from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import datetime
import selenium.common.exceptions
import time
from pymongo import MongoClient
from bs4 import NavigableString
import seleniumfactory
from fake_useragent import UserAgent

class LagouInfo:

    @classmethod
    def get_urls(cls,sourceHtml):
        soup = BeautifulSoup(sourceHtml, "lxml")
        urlList=[]
        # with open(f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_Output.html", "w",encoding='utf-8') as text_file:
        #     text_file.write(soup.prettify())
        con_list_li=soup.find("div",{"id":"s_position_list"}).find("ul",{"class":"item_con_list"}).find_all("li")

        for item in con_list_li:
            a=item.find("a",{"class":"position_link"})
            urlList.append(a["href"])
        return urlList

    @classmethod
    def insert_mongoDB(cls,collection,item):
        collection.insert_one(item)

    @classmethod
    def get_job_detail_webdriver(cls,sourceHtml,url):
            dict={}
            dict["RawUrl"]=url
            soup = BeautifulSoup(sourceHtml, "lxml")

            try:
                needLogin =  soup.find("li",{"class":"active"})
                if needLogin:
                    return dict
                
                company_dl=soup.find("dl",{"id":"job_company"})
                jobDetails=""
                for detailItem in soup.find("div",{"class":"job-detail"}).find_all("p"):
                    jobDetails+=detailItem.text
                dict["CompanyName"]=company_dl.find("em",{"class":"fl-cn"}).text.replace('\n','').strip()
                industryList =soup.find("ul",{"class":"c_feature"})  
                dict["Details"]=jobDetails.replace('\xa0','').strip()
                dict["Advantage"]=soup.find("dd",{"class":"job-advantage"}).text.replace('\n','').replace('职位诱惑：','').strip()
                dict["Location"]=soup.find("dd",{"class":"job-address clearfix"}).text.replace(" ", "").replace('\n','').replace('工作地址','').replace('查看地图','').strip()
                dict["Salary"]=soup.find("span",{"class":"ceil-salary"}).text.replace('\n','').strip()
                for industryItem in industryList:
                    if isinstance(industryItem, NavigableString):
                        continue

                    if "领域" in industryItem.text:
                        dict["Industry"]=industryItem.text.replace('\n','').replace('领域','').strip()
                        continue

                    if "发展阶段" in industryItem.text:
                        dict["Stage"]=industryItem.text.replace('\n','').replace('发展阶段','').strip()
                        continue

                    if "投资机构" in industryItem.text:
                        dict["InvestmentAgency"]=industryItem.text.replace('\n','').replace('投资机构','').strip()
                        continue

                    if "规模" in industryItem.text:
                        dict["Scale"]=industryItem.text.replace('\n','').replace('规模','').strip()
                        continue

                    if "公司主页" in industryItem.text:
                        dict["Homepage"]=industryItem.text.replace('\n','').replace('公司主页','').strip()
                        continue
                dict['Flag']=True
            except Exception as e: 
                print(f"[Error]:{url},{e}")
                dict["RawHtml"]=soup.prettify()
                dict['Flag']=False
                
            return dict
   
    @classmethod
    def insertUrlToMongo(cls,urlList,mongoClient):
        for url in urlList:
            mongoClient.insert_one(url)

    @classmethod
    def get_total_page(cls,sourceHtml):
        soup = BeautifulSoup(sourceHtml, "lxml")
        #<span class="span totalNum">30</span>
        return soup.find("span",{"class","span totalNum"}).text

    @classmethod
    def get_job_detail(cls,url):
            dict={}
            dict["RawUrl"]=url
            ua =  UserAgent()
            req = requests.get(url, headers={'User-Agent': ua.random})
            soup=BeautifulSoup(req.content.decode("utf-8"), "lxml")
            
            try:
                needLogin =  soup.find("li",{"class":"active"})
                if needLogin:
                    return dict
                
                company_dl=soup.find("dl",{"id":"job_company"})
                jobDetails=""
                for detailItem in soup.find("div",{"class":"job-detail"}).find_all("p"):
                    jobDetails+=detailItem.text
                dict["CompanyName"]=company_dl.find("em",{"class":"fl-cn"}).text.replace('\n','').strip()
                industryList =soup.find("ul",{"class":"c_feature"})  
                dict["Details"]=jobDetails.replace('\xa0','').strip()
                dict["Advantage"]=soup.find("dd",{"class":"job-advantage"}).text.replace('\n','').replace('职位诱惑：','').strip()
                dict["Location"]=soup.find("dd",{"class":"job-address clearfix"}).text.replace(" ", "").replace('\n','').replace('工作地址','').replace('查看地图','').strip()
                dict["Salary"]=soup.find("span",{"class":"ceil-salary"}).text.replace('\n','').strip()
                for industryItem in industryList:
                    if isinstance(industryItem, NavigableString):
                        continue

                    if "领域" in industryItem.text:
                        dict["Industry"]=industryItem.text.replace('\n','').replace('领域','').strip()
                        continue

                    if "发展阶段" in industryItem.text:
                        dict["Stage"]=industryItem.text.replace('\n','').replace('发展阶段','').strip()
                        continue

                    if "投资机构" in industryItem.text:
                        dict["InvestmentAgency"]=industryItem.text.replace('\n','').replace('投资机构','').strip()
                        continue

                    if "规模" in industryItem.text:
                        dict["Scale"]=industryItem.text.replace('\n','').replace('规模','').strip()
                        continue

                    if "公司主页" in industryItem.text:
                        dict["Homepage"]=industryItem.text.replace('\n','').replace('公司主页','').strip()
                        continue
                dict['Flag']=True
            except Exception as e: 
                print(f"[Error]:{url},{e}")
                dict["RawHtml"]=soup.prettify()
                dict['Flag']=False
                
            return dict
        
if __name__ == "__main__":
   
    headless = False
    urlList=[]
    browser =seleniumfactory.ChromeSelenium.init_webdirver(headless)
    # browser.get("http://whatismyipaddress.com")
    browser.get('https://www.lagou.com/jobs/list_python?px=default&yx=25k-50k&city=%E5%8C%97%E4%BA%AC#order')

    jobCollection=MongoClient('mongodb://localhost:27017/').Job.Lagou
    # urlCollection=MongoClient('mongodb://localhost:27017/').Job.LagouUrl
    wait = WebDriverWait(browser, 60)

    urlList+=LagouInfo.get_urls(browser.page_source)
    totalPage=int(LagouInfo.get_total_page(browser.page_source))

    # LagouInfo.insertUrlToMongo(LagouInfo.get_urls(browser.page_source),urlCollection)
    for num in range(0,totalPage):
        wait.until(EC.visibility_of_all_elements_located((By.ID, "s_position_list")))
        element = browser.find_element_by_class_name('pager_next ')
        time.sleep(5)
        element.click()
        time.sleep(5)
        urlList+=LagouInfo.get_urls(browser.page_source)
    
    print(f"length is {len(urlList)} details:{urlList}")

    for url in urlList:
        time.sleep(5)
        browser.get(url)
        LagouInfo.insert_mongoDB(jobCollection, LagouInfo.get_job_detail_webdriver(browser.page_source,url))
 
    browser.quit()