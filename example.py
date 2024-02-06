import streamlit as st
from st_pages import add_page_title
from streamlit_extras.switch_page_button import switch_page

add_page_title(layout="wide")
st.subheader("4) Пример функционирования", divider='green')
st.write(
    'Перед Вами несколько числовых наборов данных: площадь стран, численность населения и пример счета торговой компании. Давайте проверим их на соответствие закону первой цифры.')
st.write(
    'Выберите документ, из которого требуется извлечь числовые данные, и нажмите на кнопку «Распознать». За работу примется искусственный интеллект, который просмотрит весь документ и найдет в нем последовательность чисел.')

col1,col2 = st.columns(2)
with col1:
    if st.button('Предыдущая страница'):
        switch_page("3. структура.")
with col2:
    if st.button('Следующая страница'):
        switch_page("5. вопросы.")