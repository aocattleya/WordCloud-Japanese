# coding: utf-8
from wordcloud import WordCloud
import re


with open('analyze_Text.txt', 'r') as f:
    text = f.read()

'''------------
ローマ字を全て削除
------------'''
romaji = re.compile("[a-zA-Z]+")
text = romaji.sub("", text)


'''--------------------
3文字以下の カタカナ を削除
--------------------'''
found_katanaka_list = []
four_text_list = []
pos = 0
katanaka_pattern = re.compile('[ァ-ヴ]+')

while True:

    match1 = katanaka_pattern.search( text, pos )

    if match1 == None:
        break

    # 見つかったカタカナの後からループ開始
    pos = match1.end( 0 )

    found_katanaka_list.append(match1[0])

for katakana_words in found_katanaka_list:

    # 文字数指定
    if len(katakana_words) >= 4:
        four_text_list.append(katakana_words)

text = katanaka_pattern.sub(" ", text)

for katakana in four_text_list:
    text += " " + katakana + " "


'''--------------------
4文字以下の ひらがな を削除
--------------------'''
found_hiragana_list = []
five_text_list = []
pos = 0
hiragana_pattern = re.compile('[ぁ-ん]+')

while True:

    match2 = hiragana_pattern.search( text, pos )

    if match2 == None:
        break

    pos = match2.end( 0 )

    found_hiragana_list.append(match2[0])

for hiragana_words in found_hiragana_list:

    # 文字数指定
    if len(hiragana_words) >= 5:
        five_text_list.append(hiragana_words)

text = hiragana_pattern.sub(" ", text)

for hiragana in five_text_list:
    text += " " + hiragana + " "


'''----------------
2文字以下の 漢字 を削除
----------------'''
found_kanzi_list = []
three_text_list = []
pos = 0
kanzi_pattern = re.compile('[一-龥]+')

while True:

    match3 = kanzi_pattern.search( text, pos )

    if match3 == None:
        break

    pos = match3.end( 0 )
    found_kanzi_list.append(match3[0])

for kanzi_words in found_kanzi_list:

    # 文字数指定
    if len(kanzi_words) >= 3:
        three_text_list.append(kanzi_words)

text = kanzi_pattern.sub(" ", text)

for kanzi in three_text_list:
    text += " " + kanzi + " "


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