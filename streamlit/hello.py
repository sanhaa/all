import streamlit as st

# 페이지 제목
st.title('Hello, Streamlit!')

# 사용자 입력 받기
name = st.text_input('What is your name?')

if name:
    st.write(f'Hello, {name}!')
else:
    st.write('Hello, Stranger!')