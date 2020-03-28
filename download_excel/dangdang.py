import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from pandas import ExcelWriter

s = requests.session()
dict ={}
dict["书名"]=[]
dict["出版时间"]=[]
dict["出版社"]=[]
dict["作者"]=[]
dict["折扣价"]=[]
dict["定价"]=[]
dict["折扣"]=[]

def download(url):
    response = s.get(url,verify=False)
    return response.text

def init_data(text):
    soup =BeautifulSoup(text,features="lxml")
    for to_item in soup.find("ul",{'class':'bang_list clearfix bang_list_mode'}).find_all('li'):
        no_str=to_item.find("div",{"class":"list_num"}).text
        try:
            for book_item in to_item.find_all("div",{"class":"name"}):
                dict["书名"].append(f'=HYPERLINK("{book_item.find_all("a")[0]["href"]}", "{book_item.text}")')
                
            for publish_item in to_item.find_all("div",{"class":"publisher_info"}):
                span = publish_item.find("span")
                if span:
                        dict["出版时间"].append(span.text)
                        dict["出版社"].append(publish_item.find("a").text)
                else:
                        # dict["作者"].append(publish_item.find("a").text)
                        dict["作者"].append(publish_item.text)

            for nprice_item in to_item.find_all("span",{"class":"price_n"}):
                dict["折扣价"].append(nprice_item.text)

            for rprice_item in to_item.find_all("span",{"class":"price_r"}):
                dict["定价"].append(rprice_item.text)

            for sprice_item in to_item.find_all("span",{"class":"price_s"}):
                dict["折扣"].append(sprice_item.text)  
        except  Exception as e:
            print(f'{no_str}:{e}')

def save_log_to_excel(dict_data,file_name):
    df = pd.DataFrame(data=dict_data,index=False)
    df.to_excel(file_name)

def data_analysis():
    xl_file = pd.read_excel('dangdang.xlsx')
    # publisher=Counter(xl_file['出版社'])
    # print(publisher)
    # https://blog.algorexhealth.com/2018/03/almost-10-pie-charts-in-10-python-libraries/
    # Pie Chart 6: cufflinks
    # publisher = pd.Index(xl_file['出版社'])
    # publisher.value_counts().to_csv('kaijuan_count.csv')
    
    price = xl_file['定价']
    count_intervals(price)

def count_intervals(lst):
    intervals = []
    intervals.append(0)
    for i in range(1,16):
        intervals.append(i*20)
    
    pd.cut(lst, intervals).value_counts(sort = False).to_excel('dangdang_price.xlsx')

def convert_json():
    df = pd.read_excel('count.xlsx')
    r = df.set_index('publisher').T.to_dict('record')
    r = json.dumps(r[0],ensure_ascii=False)
    print(r)

def add_link():
    df = pd.DataFrame({'link':['=HYPERLINK("http://www.bing.com", "some website")']})
    df.to_excel('test.xlsx')

def count_nationality():
    df = pd.read_excel('dangdang_2018.xlsx')
    # df = df.assign(e=pd.Series(np.random.randn(sLength)).values)
    publisher = df['作者']
    count_import=0
    count_local=0
    lst=[]
    for item in publisher:
        try:
            if item:
                if '[' in item or '(' in str(item) or '（' in item or '【' in item or '〔' in item or '译' in item or '・' in item or '［' in item or '?' in item or '？' in item:
                    count_import+=1
                    lst.append('进口')
                else:
                    count_local+=1
                    lst.append('原创')

        except Exception as e:
            lst.append('')
            print(item)

    df = df.assign(e=pd.Series(lst).values)
    df.to_excel('dangdang_2018_kind.xlsx',index=False)

def filter_column():
    df = pd.read_excel('开卷+19年销排序+少儿绘本前500.xls')
    str_list=['情商','情绪','行为','习惯','幼儿园','性教育','成长','性格','自我保护','安全','强大内心','自我意识']
    writer = ExcelWriter('PythonExport.xlsx')
    for str_item in str_list:
        # df_query = df[df['书名'].str.contains(str_item)]
        # df_query.to_excel(f'{str_item}.xlsx')
        df[df['书名'].str.contains(str_item)].to_excel(writer,str_item, index=False)
    writer.save()

def count_string():
    df = pd.read_excel('开卷+19年销排序+少儿绘本前500.xls')
    title = df['书名']
    str_list=['情商','情绪','行为','习惯','幼儿园','性教育','成长','性格','自我保护','安全','强大内心','自我意识']
    dic={}
    dic['Name']=[]
    dic['Count']=[]

    for str_item in str_list:
        count = 0
        for title_item in title:
            if str_item in title_item:
                count += 1
        dic['Name'].append(str_item)
        dic['Count'].append(count)

    save_log_to_excel(dic,'FrequencyOfOccurrence.xlsx')

if __name__ == '__main__':
    # for i in range(1,26):
    #     url =f'http://bang.dangdang.com/books/childrensbooks/01.41.70.00.00.00-year-2018-0-1-{i}-bestsell'
    #     print("handling "+url)
    #     init_data(download(url))

    # url = 'http://bang.dangdang.com/books/childrensbooks/01.41.70.00.00.00-year-2018-0-1-10-bestsell'
    # init_data(download(url))
    # save_log_to_excel(dict,'dangdang_2018.xlsx')
    
    # count_string()
    count_nationality()
    print("job done")
    # data_analysis()
    # add_link()