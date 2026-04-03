import yfinance as yf
import pandas as pd

df = pd.DataFrame()
print('Loading...')

df_aapl = yf.download(tickers="AAPL", period="7d", interval="1m", auto_adjust=True, progress=False)

df = pd.concat([df_aapl])

# Loại bỏ trùng lặp & sắp xếp
df = df[~df.index.duplicated(keep='first')]
df.sort_index(inplace=True)

print(f"\nTổng số điểm dữ liệu thô: {len(df)}")

# ================== LÀM SẠCH DỮ LIỆU ==================
# Reset + clean header thừa thông minh
df = df.reset_index()
# Drop mọi dòng có "Ticker" hoặc toàn rỗng
df = df[~df.apply(lambda row: row.astype(str).str.contains('Ticker|Datetime,,,,,').any(), axis=1)]
df = df.dropna(how='all').reset_index(drop=True)

df.to_csv('data.csv', index=False)
