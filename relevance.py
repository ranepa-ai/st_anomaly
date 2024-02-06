import streamlit as st

from pathlib import Path
from st_pages import add_page_title
from streamlit_extras.switch_page_button import switch_page


#with st.echo("below"):
from st_pages import Page, add_page_title, show_pages

add_page_title(layout="wide")
## Declaring the pages in your app:
#add_page_title()  # Optional method to add title and icon to current page

show_pages(
    [
        Page("find_anomaly01/relevance.py", "1. Актуальность.", "🚨"),
        # Can use :<icon-name>: or the actual icon
        Page("find_anomaly01/whoisclient.py", "2. Кому интересно?", "👨‍💻"),
        # The pages appear in the order you pass them
        Page("find_anomaly01/structure.py", "3. Структура.", "📖"),
        Page("find_anomaly01/example.py", "4. Пример.", "✏️"),
        # Will use the default icon and name based on the filename if you don't
        # pass them
        Page("find_anomaly01/questions.py","5. Вопросы.", "🧰")
    ]
)


st.subheader("1) Актуальность тематики", divider='green')
st.write('Каждый из нас хоть раз сталкивался с досадной ситуацией, когда обсчитали на кассе. Впрочем, в случае с покупками, это несложно проверить, сверив цифры в чеке. Но что делать, если ошибка закралась в многотомную финансовую или налоговую отчетность? Тем более, если это не случайность, а намеренная фальсификация данных с целью мошенничества?')
st.write('Исследователями было установлено, что существуют наборы данных, в которых можно выявить возможную фальсификацию с помощью закона первой цифры (закон Бенфорда). Простыми словами этот закон можно сформулировать так: в числах, входящих в набор данных, первая цифра будет единицей примерно в 6 раз чаще, чем девяткой, и это соотношение не изменится при масштабировании исходного набора. Соответственно, при отклонении от этого правила можно предположить фальсификацию данных.')
st.write('В данной работе студенту предлгается на практике проверить работу закона первой цифры (закон Бенфорда). ')
with st.expander('Историческая справка', expanded=False):
    st.write('Астроном, математик и экономист из США Саймон Ньюкомб в 1881 году по долгу службы листал справочник по логарифмам.')
    st.write('В наше время логарифм можно взять на любом инженерном микрокалькуляторе, но в 19 веке таблицы логарифмов были для ученых, занятых точными науками, жизненно необходимыми.')
    st.write('Ньюкомб обладал проницательным умом (чему свидетельство примерно 400 научных работ) и обратил внимание на странный факт.')
    st.write('Страницы, где находились логарифмы чисел были изрядно истрепаны, а те страницы где логарифмы начинаются с 9 выглядят почти как новые.')
    st.write('Получалось так, что людей, ранее пользовавшихся книгой, интересовали числа, начинающиеся на 1, и практически не интересовали числа, начинающиеся на 9. Объяснить этот феномен Ньюкомб не смог, ведь, согласно теории вероятности, частота открытия любых страниц должна совпадать. Вскоре о странном открытии забыли.')
    st.write('Повторно обратил внимание на указанный феномен Фрэнк Бенфорд. Он анализировал табличные данные, касающиеся абсолютно несвязанных между собой понятий. В число анализа попали бассейны 335 крупнейших рек планеты, удельная теплоемкость различных веществ, уличные номера домов и многое другое. После обработки массива информации стало ясно, что в качестве первой значащей цифры числа единица появляется с вероятностью 30%. Для числа 2 эта вероятность уменьшается до 18%, а для 9 составляет всего 4,6%')
    st.write('А в 1995 году математик из США Марк Нигрини впервые предложил использовать закон Бенфорда для анализа данных налоговых деклараций, что позволило выявить случаи махинаций и сокрытия доходов.')

st.write('Вот некоторые примеры данных, удовлетворяющих закону Бенфорда:\n'
         '* 1. Площадь стран, водоемов, бассейнов рек, размеры островов;\n'
         '* 2. Численность населения стран и городов, а также показатели, основывающиеся на численности населения – к примеру, результаты выборов;\n'
         '* 3. Налоговая и финансовая отчетность;\n'
         '* 4. Показатели изменений на финансовых рынках;\n'
         '* 5. Тиражи газет и книг.')
if st.button('Следующая страница '):
    switch_page("2. кому интересно?")
