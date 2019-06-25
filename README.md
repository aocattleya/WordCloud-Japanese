### WordCloudでMecab（形態素解析エンジン）を使用せずに自力で形態素解析チックな表示を実現してみた。


インストールの複雑な『**Mecab**』を使用せずに日本語に対応したWordCloudを作成します。  
WordCloudのインストールと、100行目付近のfont_pathで日本語フォントのパスを指定する必要があります。  

以下内容は、私のTwitterの過去全ツイートでの分析

## ・[visualwords.py](https://github.com/aocattleya/WordCloud-Japanese_Sample/blob/master/visualwords.py)

![wordcloud](https://user-images.githubusercontent.com/39142850/60110631-5c934a00-97a7-11e9-8a78-4c711541747a.png)

　　  
## ・[default_visualwords.py](https://github.com/aocattleya/WordCloud-Japanese_Sample/blob/master/default_visualwords.py)

![wordcloud](https://user-images.githubusercontent.com/39142850/59966720-5f016400-955b-11e9-9f97-e1ef8ffe5f36.png)

-----

#### ・進行形で修正中
ひらがなが全て消えている。  
※見た目が悪かったら無し  

#### 検討中
漢字二文字以下を消す。  

#### 課題点
"漢字とひらがな"の混ざった単語が消えてしまう。（君の名は。 など）

-----

#### ※本来のMecab無し

英語（スペース区切り）に対応している為、繋がっている日本語文章は上手く表示されません。

![2](https://user-images.githubusercontent.com/39142850/60111648-4c7c6a00-97a9-11e9-9e82-85ab02156f65.png)
