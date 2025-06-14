import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title(" Real-Time Stock Price Dashboard")


ticker = st.text_input("Enter stock symbol (e.g., AAPL, TSLA, INFY.NS):")


if ticker:
    stock = yf.Ticker(ticker)
    data = stock.history(period="1mo")  

    if not data.empty:
        
        st.subheader(f"Showing data for: {ticker.upper()}")

        
        st.write(data)

        
        st.line_chart(data['Close'])

        
        st.subheader("Candlestick Chart")
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            increasing_line_color='green',
            decreasing_line_color='red'
        )])
        fig.update_layout(xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)
    else:
        st.warning("No data found for this ticker.")
else:
    st.info("Please enter a stock symbol to get started.")
