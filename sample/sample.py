# coding: utf-8
from wordcloud import WordCloud

text = "Chief Justice Roberts, President Carter, President Clinton, President \
        Bush, President Obama, fellow Americans, and people of the world: \
        thank you. We, the citizens of America, are now joined in a great \
        national effort to rebuild our country and to restore its promise for \
        all of our people. \
        Together, we will determine the course of America and the world for \
        years to come. \
        We will face challenges. We will confront hardships. But we will get \
        the job done. \
        Every four years, we gather on these steps to carry out the orderly \
        and peaceful transfer of power, and we are grateful to President Obama \
        and First Lady Michelle Obama for their gracious aid throughout this \
        transition. They have been magnificent."

wordcloud = WordCloud(background_color="white",
    font_path="/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf",
    width=800,height=600).generate(text)

wordcloud.to_file("./wordcloud_sample.png")