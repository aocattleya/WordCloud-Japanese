### WordCloudでMecab（形態素解析エンジン）を使用せずに形態素解析チックな表示するスクリプト


インストールの複雑な『**Mecab**』を使用せずに日本語に対応したWordCloudを作成します。  

## :cloud: インストール
```
pip install wordcloud
```

## 使い方

右上の緑ボタン`Clone or download`からダウンロード又はクローンします。

```
$ git clone https://github.com/aocattleya/WordCloud-Japanese.git
```
  　
  
後は仕様どうりです。  
・ **default_visualwords.py（デフォルトのWordCloudを作成）**  
・ **visualwords.py（猫型のWordCloudを作成　変更可）**  
の二つがあります。

スクリプト内にある`WordCloudの設定`のフォントの設定に注意してください。

```
font_path="/system/Fonts/ヒラギノ角ゴシック W4.ttc"
```

## :book: 仕様

### 詳しい内容：Qiita

[【Python】WordCloudで日本語をMecabを使用せずに形態素解析チックな表示を実現する](https://qiita.com/aocattleya/items/5be843f7de5e8fd0cfce)

---

**・見栄えの為に以下の単語を削除しています。**

　a〜Z　全て

変更する場合はソースの修正箇所にコメントを残しています。

　ひらがな　4文字以下  
　カタカナ　3文字以下  
　漢字　　　2文字以下  

　  

**・分析したい文章テキストを以下ファイルに上書きして実行します。**  
　[analyze_text.txt](https://github.com/aocattleya/WordCloud-Japanese_Sample/blob/master/analyze_text.txt)  
　  

**・`# WordCloudの設定` とコメントを残している箇所でフォントのパスを設定する。**  
　デフォルトではMac用にしています。  
　  
 
## :shipit: サンプル
私のTwitterの過去全ツイートでの分析

## ・[visualwords.py](https://github.com/aocattleya/WordCloud-Japanese_Sample/blob/master/visualwords.py)

![wordcloud](https://user-images.githubusercontent.com/39142850/60393830-8907e700-9b56-11e9-9e71-aefd840ce290.png)  
　　  

## ・[default_visualwords.py](https://github.com/aocattleya/WordCloud-Japanese_Sample/blob/master/default_visualwords.py)

![wordcloud](https://user-images.githubusercontent.com/39142850/59966720-5f016400-955b-11e9-9f97-e1ef8ffe5f36.png)

　  
　  
　  

## 本来のMecab無し

英語（スペース区切り）に対応している為、繋がっている日本語文章は正しく表示出来ません。

<img src="https://user-images.githubusercontent.com/39142850/60111648-4c7c6a00-97a9-11e9-9e82-85ab02156f65.png" width=50%>

## 🎫 License

- [MIT](https://raw.githubusercontent.com/aocattleya/WordCloud-Japanese/master/LICENSE)  
