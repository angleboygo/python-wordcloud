import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 读取整个文本
with open('yes-minister.txt','r',encoding='utf8')as f:
     text=f.read()


# 生成一个词云图像

wordcloud = WordCloud(collocations=False,font_path=font,width=1400, height=1400, margin=2).generate(text)

# 数据显示
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()


