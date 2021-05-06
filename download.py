import yfinance

df = yfinance.download('AAPL', start='2020-01-01', end='2021-05-05')
df.to_csv('AAPL.csv')
