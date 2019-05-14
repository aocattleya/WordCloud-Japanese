# coding: utf-8
from wordcloud import WordCloud

with open( 'ao.txt', 'r' ) as f:
    text = f.read()


wordcloud = WordCloud(background_color="white",
    font_path="/Library/Fonts/Verdana.ttf",
    width=800,height=600).generate(text)

wordcloud.to_file("./wordcloud_sample.png")