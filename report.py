__author__="teacher"
import random
import streamlit as st


# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
 
x=st.number_input("請輸入%g到%g之間的整數:"%(st.session_state.start,st.session_state.end)) 
confirm_input2 = st.button('輸入確認')
if confirm_input2:
 if x==st.session_state.c:
   st.write("恭喜你中獎了")
 elif x>st.session_state.c:
  if x>=st.session_state.end:
   st.write("輸入不合法,請重新輸入:")
  else:
   st.session_state.end=x
 else:
  if x<=st.session_state.start:
   st.write("輸入不合法,請重新輸入:")
  else:
   st.session_state.start=x
confirm_input = st.button('確認產生答案')
if 'start' not in st.session_state:
    st.session_state['start'] = 'value'
if 'end' not in st.session_state:
    st.session_state['end'] = 'value'  
if confirm_input:
 st.session_state.c = c = random.randint(2,99)
 st.session_state.start = 1
 st.session_state.end = 100
 st.session_state.start,st.session_state.end = 1,100
 st.write('c=', st.session_state.c)
