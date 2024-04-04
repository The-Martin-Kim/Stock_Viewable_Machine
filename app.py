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

    code = st.text_input('종목 코드', value='',
                         placeholder='종목 코드를 입력해 주세요')

start_date_str = start_date.strftime('%Y%m%d')
end_date_str = end_date.strftime('%Y%m%d')

if start_date > end_date:
    st.error('시작일은 종료일보다 이전이어야 합니다. 날짜 범위를 다시 설정해 주세요.')
else:
    if code:
        try:
            ticker_name = stock.get_market_ticker_name(code)
            st.header(f'{ticker_name} {code}')

            start_date_str = start_date.strftime('%Y%m%d')
            end_date_str = end_date.strftime('%Y%m%d')

            df = stock.get_market_ohlcv(start_date_str, end_date_str, code)
            data = df.sort_index(ascending=True).loc[:, '종가']

            tab1, tab2 = st.tabs(['Chart', 'Data'])

            with tab1:
                st.line_chart(data)

            with tab2:
                st.dataframe(df.sort_index(ascending=False))

        except ValueError:
            st.error('유효하지 않은 종목 코드입니다. 정확한 종목 코드를 입력해 주세요.')
