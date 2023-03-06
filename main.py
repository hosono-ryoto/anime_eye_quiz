import streamlit as st
from PIL import Image

count = 0

st.title('アニメ「目」クイズ！！')

st.header('あそびかた')
expander1 = st.expander('1.キャラクターの目だけを見て当てよう！')
expander1.write('難易度はかんたんだよ！')
expander2 = st.expander('2.キャラ名はフルネームで！(ひらがなも可)')
expander2.write('正しく判定できないよ！')
expander3 = st.expander('3.問題は全部で10問！')
expander3.write('全問正解を目指そう！')

st.write('問1')
img1 = Image.open('eye/nadeshiko_eye.jpg')
st.image(img1)

text = st.text_input(key=1, label='回答')
if text == '各務原なでしこ':
    '◯正解！'
    img = Image.open('character/nadeshiko.jpg')
    st.image(img, caption = 'ゆるキャン△：各務原なでしこ')
    count += 1
elif text == 'かがみはらなでしこ':
    '◯正解！'
    img = Image.open('character/nadeshiko.jpg')
    st.image(img, caption = 'ゆるキャン△：各務原なでしこ')
    count += 1
elif not text:
    '' 
else:
    '✕残念！'

st.write('問2')
img = Image.open('eye/eriri_eye.jpg')
st.image(img)

text = st.text_input(key=2, label='回答')
if text == '澤村スペンサー英梨々':
    '◯正解！'
    img = Image.open('character/eriri.jpg')
    st.image(img, caption = '冴えない彼女の育て方：澤村スペンサー英梨々')
    count += 1
elif text == 'さわむらすぺんさーえりり':
    '◯正解！'
    img = Image.open('character/eriri.jpg')
    st.image(img, caption = '冴えない彼女の育て方：澤村スペンサー英梨々')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問3')
img = Image.open('eye/suzune_eye.jpg')
st.image(img)

text = st.text_input(key=3, label='回答')
if text == '堀北鈴音':
    '◯正解！'
    img = Image.open('character/suzune.jpg')
    st.image(img, caption = 'ようこそ実力至上主義の教室へ：堀北鈴音')
    count += 1
elif text == 'ほりきたすずね':
    '◯正解！'
    img = Image.open('character/suzune.jpg')
    st.image(img, caption = 'ようこそ実力至上主義の教室へ：堀北鈴音')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問4')
img = Image.open('eye/hinami_eye.jpg')
st.image(img)

text = st.text_input(key=4, label='回答')
if text == '笛口雛実':
    '◯正解！'
    img = Image.open('character/hinami.jpg')
    st.image(img, caption = '東京喰種：笛口雛実')
    count += 1
elif text == 'ふえぐちひなみ':
    '◯正解！'
    img = Image.open('character/hinami.jpg')
    st.image(img, caption = '東京喰種：笛口雛実')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問5')
img = Image.open('eye/ruka_eye.jpg')
st.image(img)

text = st.text_input(key=5, label='回答')
if text == '更科瑠夏':
    '◯正解！'
    img = Image.open('character/ruka.jpg')
    st.image(img, caption = '彼女、お借りします：更科瑠夏')
    count += 1
elif text == 'さらしなるか':
    '◯正解！'
    img = Image.open('character/ruka.jpg')
    st.image(img, caption = '彼女、お借りします：更科瑠夏')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問6')
img = Image.open('eye/eru_eye.jpg')
st.image(img)

text = st.text_input(key=6, label='回答')
if text == '千反田える':
    '◯正解！'
    img = Image.open('character/eru.jpg')
    st.image(img, caption = '氷菓：千反田える')
    count += 1
elif text == 'ちたんだえる':
    '◯正解！'
    img = Image.open('character/eru.jpg')
    st.image(img, caption = '氷菓：千反田える')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問7')
img = Image.open('eye/miduki_eye.jpg')
st.image(img)

text = st.text_input(key=7, label='回答')
if text == '柴田美月':
    '◯正解！'
    img = Image.open('character/miduki.jpg')
    st.image(img, caption = '魔法科高校の劣等生：柴田美月')
    count += 1
elif text == 'しばたみづき':
    '◯正解！'
    img = Image.open('character/miduki.jpg')
    st.image(img, caption = '魔法科高校の劣等生：柴田美月')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問8')
img = Image.open('eye/maki_eye.jpg')
st.image(img)

text = st.text_input(key=8, label='回答')
if text == '西木野真姫':
    '◯正解！'
    img = Image.open('character/maki.jpg')
    st.image(img, caption = 'ラブライブ！：西木野真姫')
    count += 1
elif text == 'にしきのまき':
    '◯正解！'
    img = Image.open('character/maki.jpg')
    st.image(img, caption = 'ラブライブ！：西木野真姫')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問9')
img = Image.open('eye/yukino_eye.jpg')
st.image(img)

text = st.text_input(key=9, label='回答')
if text == '雪ノ下雪乃':
    '◯正解！'
    img = Image.open('character/yukino.jpg')
    st.image(img, caption = 'やはり俺の青春ラブコメはまちがっている。：雪ノ下雪乃')
    count += 1
elif text == 'ゆきのしたゆきの':
    '◯正解！'
    img = Image.open('character/yukino.jpg')
    st.image(img, caption = 'やはり俺の青春ラブコメはまちがっている。：雪ノ下雪乃')
    count += 1
elif not text:
    ''
else:
    '✕残念！'

st.write('問10')
img = Image.open('eye/ayumi_eye.jpg')
st.image(img)

text = st.text_input(key=10, label='回答')
if text == '乙坂歩未':
    '◯正解！'
    img = Image.open('character/ayumi.jpg')
    st.image(img, caption = 'Charlotte：乙坂歩未')
    count += 1
elif text == 'おとさかあゆみ':
    '◯正解！'
    img = Image.open('character/ayumi.jpg')
    st.image(img, caption = 'Charlotte：乙坂歩未')
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
