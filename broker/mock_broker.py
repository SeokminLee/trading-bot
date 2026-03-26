import yfinance as yf

def run_mock(ticker='AAPL'):
    print(f'Running mock broker for {ticker}')
    data = yf.download(ticker, period='1mo', interval='1d')
    print(data[['Open','High','Low','Close']].tail())
