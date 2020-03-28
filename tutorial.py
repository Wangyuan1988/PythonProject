# coding=utf8
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from pymongo import MongoClient


jobCollection=MongoClient('mongodb://localhost:27017/').Job.Lagou

content=''
for item in jobCollection.find({},{'Details':1}):
    if item["Details"]:
        content+=item["Details"]

font=r'C:/Users/Kevin/Downloads/SourceHanSansCN/SourceHanSansCN-Normal.otf' 
seg_list = jieba.cut(content, cut_all=False)
wl_space_split = " ".join(seg_list)
 
my_wordcloud = WordCloud(font_path=font,width=1800,height=1000,max_font_size=84,min_font_size=16).generate(wl_space_split)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()