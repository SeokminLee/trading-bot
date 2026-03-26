import streamlit as st
from backtest.run_backtest import run_backtest

st.title('Trading Bot Dashboard')
ticker = st.text_input('Ticker', 'AAPL')
if st.button('Run backtest'):
    equity = run_backtest(ticker)
    st.line_chart(equity)
