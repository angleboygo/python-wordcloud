from wordcloud import WordCloud
import matplotlib.pyplot as plt
# 自定义画板
with open('yes-minister.txt', 'r', encoding='utf8')as f:
    text = f.read()

font=r'C:\Windows\Fonts\STZHONGS.TTF'
wc=WordCloud(
    background_color='white',
    max_words=200,
    font_path=font,
    min_font_size=15,
    max_font_size=50,
    width=400,
)

wc.generate(text)
wc.to_file('自定义图片.png')

plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()