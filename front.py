import streamlit as st



# タイトルとディスクリプションの設定
st.title('リサーチの習慣化')
st.write('目の前が霧で立ち込めて見えない時')
st.write('それは、自分の爪を研ぐ時間')

habit=st.selectbox("朝の習慣リスト",["筋トレ","論文","起業関連","プログラミング"])

"朝の習慣は",habit


# セットアップの定義
st.sidebar.subheader('設定')
sex = st.sidebar.selectbox('性別', ('男性', '女性'))
age = st.sidebar.slider('年齢', min_value=0, max_value=120, step=1)

'性別',sex
'年齢',age
st.date_input('あなたの誕生日を入力してください。')

uploaded_file = st.file_uploader("画像を選択", type= ["jpg", "png"])
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  #img_path = f'img/{uploaded_file.name}'
  #img.save(img_path)
  st.image(img)
