import streamlit as st
from PIL import Image

count = 0

st.title('アニメ「目」クイズ！！')

st.header('あそびかた')
expander1 = st.expander('1.キャラクターの目だけを見て当てよう！')
expander1.write('難易度はかんたんだよ！')
expander2 = st.expander('2.正解すると全体画像が表示されるよ！')
expander2.write('答え合わせだね！')
expander3 = st.expander('3.問題は全部で10問！')
expander3.write('全問正解を目指そう！')

st.write('問1')
img = Image.open('eye/nadeshiko_eye.jpg')
st.image(img)

text = st.text_input(key=1, label='回答')
if text == '各務原なでしこ' or text == '各務原' or text == 'かがみはらなでしこ' or text == 'かがみはら' or text == 'なでしこ':
    '◯正解！'
    img = Image.open('character/nadeshiko.jpg')
    st.image(img, caption='ゆるキャン△：各務原なでしこ')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問2')
img = Image.open('eye/eriri_eye.jpg')
st.image(img)

text = st.text_input(key=2, label='回答')
if text == '澤村スペンサー英梨々' or text == '澤村' or text == 'スペンサー' or text == '英梨々' or text == 'さわむらすぺんさーえりり' or text == 'さわむら' or text == 'すぺんさー' or text == 'えりり':
    '◯正解！'
    img = Image.open('character/eriri.jpg')
    st.image(img, caption='冴えない彼女の育て方：澤村スペンサー英梨々')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問3')
img = Image.open('eye/suzune_eye.jpg')
st.image(img)

text = st.text_input(key=3, label='回答')
if text == '堀北鈴音' or text == '堀北' or text == '鈴音' or text == 'ほりきたすずね' or text == 'ほりきた' or text == 'すずね':
    '◯正解！'
    img = Image.open('character/suzune.jpg')
    st.image(img, caption='ようこそ実力至上主義の教室へ：堀北鈴音')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問4')
img = Image.open('eye/hinami_eye.jpg')
st.image(img)

text = st.text_input(key=4, label='回答')
if text == '笛口雛実' or text == '笛口' or text == '雛実' or text == 'ふえぐちひなみ' or text == 'ふえぐち' or text == 'ひなみ' or text == 'ヒナミ':
    '◯正解！'
    img = Image.open('character/hinami.jpg')
    st.image(img, caption='東京喰種：笛口雛実')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問5')
img = Image.open('eye/ruka_eye.jpg')
st.image(img)

text = st.text_input(key=5, label='回答')
if text == '更科瑠夏' or text == '更科' or text == '瑠夏' or text == 'さらしなるか' or text == 'さらしな' or text == 'るか':
    '◯正解！'
    img = Image.open('character/ruka.jpg')
    st.image(img, caption='彼女、お借りします：更科瑠夏')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問6')
img = Image.open('eye/eru_eye.jpg')
st.image(img)

text = st.text_input(key=6, label='回答')
if text == '千反田える' or text == '千反田' or text == 'ちたんだえる' or text == 'える':
    '◯正解！'
    img = Image.open('character/eru.jpg')
    st.image(img, caption='氷菓：千反田える')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問7')
img = Image.open('eye/miduki_eye.jpg')
st.image(img)

text = st.text_input(key=7, label='回答')
if text == '柴田美月' or text == '柴田' or text == '美月' or text == 'しばたみづき' or text == 'しばた' or text == 'みづき':
    '◯正解！'
    img = Image.open('character/miduki.jpg')
    st.image(img, caption='魔法科高校の劣等生：柴田美月')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問8')
img = Image.open('eye/maki_eye.jpg')
st.image(img)

text = st.text_input(key=8, label='回答')
if text == '西木野真姫' or text == '西木野' or text == '真姫' or text == 'にしきのまき' or text == 'にしきの' or text == 'まき':
    '◯正解！'
    img = Image.open('character/maki.jpg')
    st.image(img, caption='ラブライブ！：西木野真姫')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問9')
img = Image.open('eye/yukino_eye.jpg')
st.image(img)

text = st.text_input(key=9, label='回答')
if text == '雪ノ下雪乃' or text == '雪ノ下' or text == '雪乃' or text == 'ゆきのしたゆきの' or text == 'ゆきのした' or text == 'ゆきの':
    '◯正解！'
    img = Image.open('character/yukino.jpg')
    st.image(img, caption='やはり俺の青春ラブコメはまちがっている。：雪ノ下雪乃')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問10')
img = Image.open('eye/ayumi_eye.jpg')
st.image(img)

text = st.text_input(key=10, label='回答')
if text == '乙坂歩未' or text == '乙坂' or text == '歩未' or text == 'おとさかあゆみ' or text == 'おとさか' or text == 'あゆみ':
    '◯正解！'
    img = Image.open('character/ayumi.jpg')
    st.image(img, caption='Charlotte：乙坂歩未')
    count += 1
elif not text:
    ''
else:
    '✕残念！'


st.subheader(f'10問中{count}問正解！')
if count == 10:
    '全問正解！おめでとう！'
elif count >= 9:
    'おしい！'
elif count >= 5:
    'まずまずだね！'
else:
    'もっと頑張ろう！'
