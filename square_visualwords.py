# coding: utf-8
from wordcloud import WordCloud
import re


with open('sample.txt', 'r') as f:
    text = f.read()

seiki1 = re.compile("[a-zA-Z]+")
text = seiki1.sub("", text)

found_katakana_words = []
pattern = re.compile('[ァ-ヴ][ァ-ヴ][ァ-ヴ][ァ-ヴ][ァ-ヴ]+')

pos = 0
while True:
    a_match = pattern.search( text, pos )

    if a_match == None:
        break
    
    pos = a_match.end( 0 )

    found_katakana_words.append(a_match[0])

for x in found_katakana_words:
    text = text.replace(x, " " + x + " ")


found_hiragana_words = []
pattern2 = re.compile('[ぁ-ん]')

pos = 0
while True:
    a_match2 = pattern2.search( text, pos )

    if a_match2 == None:
        break
    
    pos = a_match2.end( 0 )

    found_hiragana_words.append(a_match2[0])

for y in found_hiragana_words:
    if len(y) <= 3:
        text = text.replace(y, "")

    else:
        text = text.replace(y, " " + y + " ")


dictText = {'を':' を ',
            'に':' に ',
            'って':' って ',
            'も':' も ',
            'は':' は ',
            'と':' と ',
            'から':' から ',
            'で':' で ',
            }

eng = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
gomi = ["キズナアイ", "した", "自分","ござ","りあえず"]

stop_text = list(dictText.keys()) + eng + gomi

for k, v in dictText.items():
    text = text.replace(k, v)

wordcloud = WordCloud(background_color="white",
                      font_path="/Library/Fonts/ヒラギノ角ゴシック W4.ttc",
                      stopwords = stop_text,
                      width=800, height=600).generate(text)

wordcloud.to_file("./wordcloud.png")