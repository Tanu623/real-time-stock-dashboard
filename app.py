import dash
from dash import dcc, html
import plotly.graph_objects as go
from src.fetch_data import get_stock_data

app = dash.Dash(__name__)

df = get_stock_data()
if df is None:
    df = []

def generate_figure():
    if len(df) == 0:
        return go.Figure()
    return go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])

app.layout = html.Div([
    dcc.Graph(figure=generate_figure())
])

if __name__ == "__main__":
    app.run_server(debug=True)
