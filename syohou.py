import streamlit as st

st.title("処方計算")
week=st.selectbox("次の外来までの週数を選択してください",list(range(0,20)))
day = week*7
"処方を",day
"日分お願いします。"
