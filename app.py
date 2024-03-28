import streamlit as st
from pykrx import stock
import datetime

st.title('Stock Price Chart Viewable Machine')

with st.sidebar:
    start_date = st.date_input(
        "시작일을 선택해 주세요",
        datetime.datetime.now() - datetime.timedelta(days=10)
    )

    end_date = st.date_input(
        "종료일을 선택해 주세요",
        datetime.datetime.now()
    )

    code = st.text_input(
        '종목 코드',
        value='',
        placeholder='종목 코드를 입력해 주세요'
    )

start_date_str = start_date.strftime('%Y%m%d')
end_date_str = end_date.strftime('%Y%m%d')

if code and start_date and end_date:
    df = stock.get_market_ohlcv(start_date_str, end_date_str, code)
    data = df.sort_index(ascending=True).loc[:, '종가']

    tab1, tab2 = st.tabs(['Chart', 'Data'])

    with tab1:
        st.line_chart(data)

    with tab2:
        st.dataframe(df.sort_index(ascending=False))
