import streamlit as st
from PIL import Image

st.title("長崎大学消化器内科実習へようこそ")
ima = Image.open('image02.png')
st.image(ima, caption='消化器内科へようこそ')

if st.button("オリエンテーション"):
  st.write("自己紹介アンケートにご協力お願いします。")
  st.text_input("ご出身高校")
  st.text_input("部活")
  st.text_input("志望の診療科")
  st.button("送信")

if st.button("ポリクリスケジュール"):
  st.write("ポリクリスケジュール")
  image = Image.open('plan.png')
  st.image(image, caption='ポリクリスケジュール')

st.sidebar.title("MENU")