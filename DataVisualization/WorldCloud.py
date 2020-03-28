# coding=utf8
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from pymongo import MongoClient

#https://amueller.github.io/word_cloud/auto_examples/wordcloud_cn.html
jobCollection=MongoClient('mongodb://localhost:27017/').Job.Lagou

content=''
for item in jobCollection.find({ "Flag" : True},{'Details':1}):
    if item["Details"]:
        content+=item["Details"]

seg_list = jieba.cut(content, cut_all=False)
wl_space_split = " ".join(seg_list)

font=r'C:/Users/Kevin/Downloads/SourceHanSansCN/SourceHanSansCN-Normal.otf' 
my_wordcloud = WordCloud(font_path=font,width=1800,height=1000,max_font_size=84,min_font_size=16).generate(wl_space_split)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()