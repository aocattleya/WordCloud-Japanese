# coding: utf-8
from wordcloud import WordCloud

with open('sample.txt', 'r') as f:
    text = f.read()

wordcloud = WordCloud(background_color="white",
                      font_path="/Library/Fonts/ヒラギノ角ゴシック W4.ttc",
                      #stopwords = [u''],
                      width=800, height=600).generate(text)

wordcloud.to_file("./wordcloud.png")
