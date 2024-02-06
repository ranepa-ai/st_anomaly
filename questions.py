import streamlit as st
from st_pages import add_page_title
from streamlit_extras.switch_page_button import switch_page

add_page_title(layout="wide")
st.session_state['count_page'] = 4
st.subheader("5) Вопросы по теме", divider='green')
yes_no = st.radio("1) Посмотрите на перечень телефонных номеров. Как Вы думаете, можно ли определить, соответствует ли она закону Бенфорда, без дополнительных вычислений?",
    ["нельзя", "можно", "можно,только с вычислениями"], index=None, )
if yes_no == 'можно':
    st.write(f":green[Правильно!]")
else:
    st.write(f":red[Неравильно!]")

spa_cy = st.radio("2) Как называется библиотека по выделению сущностей из текста?", ["spiCy", "speCy", "spaCy"],
                  index=None, )
if spa_cy == 'spaCy':
    st.write(f":green[Правильно!]")
else:
    st.write(f":red[Неравильно!]")

num_pr = st.radio("3) Как обозначаются числительные при выделении сущностей из текста?",
                  ["PROPN", "ADJ", "NUM", "NOUN"], index=None, )
if num_pr == 'NUM':
    st.write(f":green[Правильно!]")
else:
    st.write(f":red[Неравильно!]")

st.subheader('Рекомендуемая литература:')
href = f'<a href="https://www.litres.ru/book/joseph-wells-t/benford-s-law-applications-for-forensic-accounting-auditing-28299723/">1. Benfords Law. Application for Forensic Accounting, Auditing, and Fraud Detection. Mark J. Nigrini.</a> (right-click and save as &lt;some_name&gt;.csv)'
st.write(href, unsafe_allow_html=True)
st.write('2. Концепция информационного пространства финансового рынка. Диссертация на соискание ученой степени доктора экономических наук. Алексеев Михаил Анатольевич.')

col1,col2 = st.columns(2)
with col1:
    if st.button('Предыдущая страница'):
        switch_page("4. пример.")
with col2:
    href = f'<a href="http://83.143.66.61:27368/">Переход  следующему тренажеру.</a>'
    st.write(href, unsafe_allow_html=True)
