import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Fetch stock data
def get_stock_data(ticker, period='1y', interval='1d'):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period, interval=interval)
        if data.empty or 'Close' not in data.columns:
            return None
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None

# Candlestick chart
def plot_candlestick(data, stock_symbol):
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )])
    fig.update_layout(
        title_text=f'Candlestick Chart - {stock_symbol}',
        xaxis_title='Date',
        yaxis_title='Stock Price',
        xaxis_rangeslider_visible=False
    )
    return fig

# Calculate daily change
def calculate_daily_profit_loss(data):
    data['Daily Change'] = data['Close'].pct_change() * 100
    return data

# Line chart for daily profit/loss
def plot_profit_loss(data, stock_symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['Daily Change'],
        mode='lines',
        name='Daily Change'
    ))
    fig.update_layout(
        title_text=f'Daily Profit/Loss - {stock_symbol}',
        xaxis_title='Date',
        yaxis_title='Percentage Change'
    )
    return fig

# --- Streamlit UI ---

st.set_page_config(page_title="📊 Stock Analysis", layout="wide")
st.title('📊 Stock Analysis Project')

stocks = [
    'AAPL', 'GOOGL', 'MSFT', 'COIN', 'AMZN', 'MRNA', 'NVAX', 'INO', 'ARM',
    'BNTX', 'VXRT', 'NCLH', 'AZN', 'TCS', 'LBPH', 'AMD', 'HIMS', 'FIZZ',
    'CRSP', 'LPL', 'PRTA', 'USCA', 'USAC', 'YY', 'LYFT', 'LI', 'NIO', 'JOBY', 'SQ'
]

selected_stocks = st.multiselect('Select stock symbols:', stocks)
investment_amount = st.number_input('Enter your investment amount:', min_value=0.01, value=1000.0, step=0.01)

stock_data_dict = {}
for stock_symbol in selected_stocks:
    with st.spinner(f'Fetching stock data for {stock_symbol}...'):
        data = get_stock_data(stock_symbol)
    if data is None or data.empty:
        st.warning(f"No valid data found for {stock_symbol}. Please check the ticker or try a different interval.")
    else:
        data = calculate_daily_profit_loss(data)
        stock_data_dict[stock_symbol] = data
        st.success(f'Data fetched for {stock_symbol}.')

# Display stock info
for stock_symbol, stock_data in stock_data_dict.items():
    st.header(f"📈 {stock_symbol} Stock Summary")

    st.subheader('Latest Stock Data')
    st.dataframe(stock_data.tail())

    st.subheader('📉 Daily Profit/Loss')
    st.plotly_chart(plot_profit_loss(stock_data, stock_symbol), use_container_width=True)

    st.subheader('📊 Candlestick Chart')
    st.plotly_chart(plot_candlestick(stock_data, stock_symbol), use_container_width=True)

    # Investment Simulation
    if 'Daily Change' in stock_data.columns and not stock_data['Daily Change'].isnull().all():
        cumulative_return = (1 + stock_data['Daily Change'].fillna(0) / 100).cumprod()
        final_value = investment_amount * cumulative_return.iloc[-1]

        st.subheader(f'💰 Investment Simulation - {stock_symbol}')
        st.write(f'Initial Investment: ${investment_amount:,.2f}')
        st.write(f'Final Value After 1 Year: ${final_value:,.2f}')

        if final_value > investment_amount:
            st.success("You made a profit!")
        elif final_value < investment_amount:
            st.error("You incurred a loss.")
        else:
            st.info("No profit, no loss. Value remained unchanged.")
    else:
        st.warning("Not enough valid data to simulate investment performance.")