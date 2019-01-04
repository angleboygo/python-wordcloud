from wordcloud import WordCloud
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np


# 数据准备
with open('data1.txt','r',encoding='utf8') as f:
    text=f.read()

# 图片读取
football=np.array(Image.open('红心.jpg'))


# 数据清洗（分词）
font=r'C:\Windows\Fonts\STZHONGS.TTF'
wordcloud = WordCloud(max_font_size=30,font_path=font,mask=football).generate(text)

# 数据显示
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()




