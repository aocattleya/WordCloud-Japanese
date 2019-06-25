# coding: utf-8
from wordcloud import WordCloud
import re
from PIL import Image
import numpy as np

# 背景画像の読み込み
mask = np.array(Image.open('cat.png'))
mask = np.where(mask == 0, 0, 255)

# テキストの読み込み
with open('analyze_Text.txt', 'r') as f:
    text = f.read()


# ローマ字を全て削除
romaji = re.compile("[a-zA-Z]+")
text = romaji.sub("", text)


# カタカナの削除
found_katakana_words = []
katakana_pattern = re.compile('[ァ-ヴ][ァ-ヴ][ァ-ヴ][ァ-ヴ][ァ-ヴ]+')

pos = 0
while True:
    # textの中からカタカナを検索
    match1 = katakana_pattern.search( text, pos )

    # 無ければ終了
    if match1 == None:
        break
    
    # 次のループを、見つかったカタカナの後から開始させる
    pos = match1.end( 0 )

    # 見つかったカタカナをリストに入れる
    found_katakana_words.append(match1[0])

# カタカナの前後にスペースを追加
for x in found_katakana_words:
    text = text.replace(x, " " + x + " ")


# 助詞の前後にスペース追加
dictText = {'を':' を ',
            'に':' に ',
            'って':' って ',
            'も':' も ',
            'は':' は ',
            'と':' と ',
            'から':' から ',
            'で':' で ',
            }

for k, v in dictText.items():
    text = text.replace(k, v)


# ひらがなを削除
found_hiragana_words = []
hiragana_pattern = re.compile('[ぁ-ん]+')
pos = 0

while True:
    # textの中からひらがなを検索
    match2 = hiragana_pattern.search( text, pos )

    # 無ければ終了
    if match2 == None:
        break

    # 次のループを、見つかったひらがなの後から開始させる
    pos = match2.end( 0 )

    # ひらがなの前後にスペースを追加
    found_hiragana_words.append(match2[0])

# ひらがな の前後にスペースを追加
for y in found_hiragana_words:
    
    # 2文字以下の場合は削除する
    if len(y) <= 2:
        text = text.replace(y, "")

    # それ以外は前後にスペース
    else:
        text = text.replace(y, " " + y + " ")


# 任意の削除したい文字
stop = ["自分", "出来", "キズナアイ"]

# WordCloudの設定
wordcloud = WordCloud(mask = mask,
                      font_path="/system/Library/Fonts/ヒラギノ角ゴシック W4.ttc",
                      stopwords = stop,
                      # background_color="white",
                      colormap = 'copper_r',
                      # contour_width = 1,
                      # contour_color='gray',
                      width=800, height=600).generate(text)

# WordCloudを作成する
wordcloud.to_file("./wordcloud.png")