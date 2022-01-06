__author__="teacher"
import random
import streamlit as st
confirm_input = st.sidebar.button('確認產生答案')

if confirm_input:
 c = random.randint(2,99)
 start = 1
 end = 100
 start,end = 1,100
 st.write('c=', c)
 
x=st.number_input("請輸入%g到%g之間的整數:"%(start,end)) 
confirm_input2 = st.button('輸入確認')
if confirm_input2:
  if x==c:
    st.write("恭喜你中獎了")
 elif x>c:
  if x>=end:
    st.write("輸入不合法,請重新輸入:")
  else:
    end=x
 else:
   if x<=start:
    st.write("輸入不合法,請重新輸入:")
   else:
     start=x


