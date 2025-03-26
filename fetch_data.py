import yfinance as yf

def get_stock_data(ticker="AAPL"):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1mo")
        if df.empty:
            raise ValueError("No data retrieved. Check the ticker symbol.")
        return df
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None
