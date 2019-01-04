from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np

#数据获取
with open('李小璐xxx.txt','r',encoding='utf8')as f:
    text=f.read()

# 图片数据获取
cloud_img=np.array(Image.open('关羽.jpg'))

# 忽略一些词,例如

st = set(['我们','还是'])

#配置wordcloud
font=r'C:\Windows\Fonts\STZHONGS.TTF'
wc = WordCloud(
    background_color="white",
    mask=cloud_img,
    max_words=200,
    font_path=font,
    # min_font_size=15,
    max_font_size=18,
    width=400,
    stopwords=st,
    )
wc.generate(text)
wc.to_file("ccc.png") #图片保存到ccc.png

plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()



