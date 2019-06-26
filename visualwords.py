# coding: utf-8
from wordcloud import WordCloud
import re
from PIL import Image
import numpy as np


mask = np.array(Image.open('cat.png'))
mask = np.where(mask == 0, 0, 255)

with open('analyze_Text.txt', 'r') as f:
    text = f.read()


'''
ローマ字を全て削除
'''
romaji = re.compile("[a-zA-Z]+")
text = romaji.sub("", text)


'''
カタカナの前後にスペースを追加
'''
found_katakana_words = []
katakana_pattern = re.compile('[ァ-ヴ][ァ-ヴ][ァ-ヴ][ァ-ヴ][ァ-ヴ]+')
pos = 0

while True:

    match1 = katakana_pattern.search( text, pos )

    if match1 == None:
        break
    
    # 見つかったカタカナの後から開始
    pos = match1.end( 0 )

    found_katakana_words.append(match1[0])

for x in found_katakana_words:
    text = text.replace(x, " " + x + " ")


'''
5文字以下の ひらがな を削除
'''
found_hiragana_words = []
three = []
pos = 0
hiragana_pattern = re.compile('[ぁ-ん]+')

while True:

    match2 = hiragana_pattern.search( text, pos )

    if match2 == None:
        break

    # 見つかったひらがなの後から開始させる
    pos = match2.end( 0 )

    found_hiragana_words.append(match2[0])

for y in found_hiragana_words:
    if len(y) >= 5:
        three.append(y)
        text = text.replace(y, " ")

hiragana = re.compile('[ぁ-ん]+')
text = hiragana.sub(" ", text)

for t in three:
    text += " " + t + " "


'''
任意の削除したい文字
'''
stop = []


'''
WordCloudの設定
'''
wordcloud = WordCloud(mask = mask,
                      font_path="/system/Library/Fonts/ヒラギノ角ゴシック W4.ttc",
                      stopwords = stop,
                      # background_color="white",
                      colormap = 'copper_r',
                      # contour_width = 1,
                      # contour_color='gray',
                      width=800, height=600).generate(text)

wordcloud.to_file("./wordcloud.png")