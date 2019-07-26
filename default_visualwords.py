# coding: utf-8
from wordcloud import WordCloud
import re


with open('analyze_Text.txt', 'r') as f:
    text = f.read()

'''
ローマ字を全て削除
'''
seiki1 = re.compile("[a-zA-Z]+")
text = seiki1.sub("", text)

'''
3文字以下の カタカナ を削除
'''
found_katanaka_words = []
four_text_list = []
pos = 0
katanaka_pattern = re.compile('[ァ-ヴ]+')

while True:

    match1 = katanaka_pattern.search( text, pos )

    if match1 == None:
        break

    # 見つかったカタカナの後からループ開始
    pos = match1.end( 0 )

    found_katanaka_words.append(match1[0])

for a in found_katanaka_words:

    # 文字数指定
    if len(a) >= 4:
        four_text_list.append(a)

text = katanaka_pattern.sub(" ", text)

for b in four_text_list:
    text += " " + b + " "


'''
4文字以下の ひらがな を削除
'''
found_hiragana_words = []
five_text_list = []
pos = 0
hiragana_pattern = re.compile('[ぁ-ん]+')

while True:

    match2 = hiragana_pattern.search( text, pos )

    if match2 == None:
        break

    pos = match2.end( 0 )

    found_hiragana_words.append(match2[0])

for c in found_hiragana_words:

    # 文字数指定
    if len(c) >= 5:
        five_text_list.append(c)

hiragana = re.compile('[ぁ-ん]+')
text = hiragana.sub(" ", text)

for d in five_text_list:
    text += " " + d + " "


'''
2文字以下の 漢字 を削除
'''
found_kanzi_words = []
three_text_list = []
pos = 0
kanzi_pattern = re.compile('[一-龥]+')

while True:

    match3 = kanzi_pattern.search( text, pos )

    if match3 == None:
        break

    pos = match3.end( 0 )
    found_kanzi_words.append(match3[0])

for e in found_kanzi_words:

    # 文字数指定
    if len(e) >= 3:
        three_text_list.append(e)

text = kanzi_pattern.sub(" ", text)

for f in three_text_list:
    text += " " + f + " "


'''
任意の削除したい単語
'''
stop = ["ピヨピヨ", "ホゲホゲ"]


'''
WordCloudの設定
'''
wordcloud = WordCloud(background_color="white",
                      font_path="/system/Fonts/ヒラギノ角ゴシック W4.ttc",
                      stopwords = stop,
                      width=800, height=600).generate(text)

wordcloud.to_file("./wordcloud.png")