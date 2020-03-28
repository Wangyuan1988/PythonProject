# coding=utf8
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from os import path
import os
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, 'luoshenfu.txt'),'r', encoding='UTF-8').read()
alice_coloring = np.array(Image.open(path.join(d, "alice.png")))
stopwords = set(STOPWORDS)
stopwords.add("。")
stopwords.add("，")

font=path.join(d,'SourceHanSansCN-Normal.otf') 
my_wordcloud = WordCloud(mask=alice_coloring,font_path=font,max_font_size=40,background_color="white",random_state=42,stopwords=stopwords).generate(text)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.imshow(my_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()