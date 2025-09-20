📊 Stock Model Analysis

An interactive Streamlit-based web application that helps users analyze stock market performance, visualize stock charts, and simulate investments.
It fetches real-time historical data from Yahoo Finance and provides insightful visualizations such as candlestick charts, daily profit/loss trends, and investment growth simulations.


✨ Key Features

✅ Stock Data Fetching

Retrieves stock history (1 year by default, daily interval) using yfinance.

Handles errors gracefully if a ticker symbol is invalid or no data is found.

✅ Candlestick Chart

Interactive Plotly candlestick visualization.

Shows Open, High, Low, and Close prices over time.

Ideal for traders who want to see price action trends.

✅ Daily Profit/Loss Chart

Calculates percentage change in closing prices.

Displays trends as a line chart to highlight volatility.

✅ Investment Simulation

Enter an investment amount (default: $1000).

Calculates how much your investment would be worth after 1 year.

Gives clear feedback: 🟢 profit, 🔴 loss, or ⚪ neutral.

✅ Multi-stock Selection

Choose one or multiple stocks from a predefined list of popular tickers (e.g., AAPL, GOOGL, MSFT, AMZN, AMD, NIO, etc.).

Data is processed individually and displayed in a clean layout.

✅ User-Friendly Interface

Built with Streamlit, ensuring an interactive and easy-to-use UI.

Responsive wide-layout design for better chart visibility.


🛠️ Tech Stack

Python – core programming language

Streamlit – interactive web UI

yfinance – fetches real-world stock data

pandas – data manipulation & calculations

plotly – advanced charting & visualization


📂 Project Structure
📦 Stock Model Analysis
 ┣ 📜 app.py              # Main Streamlit app
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 📜 README.md           # Documentation


📦 Installation

Clone the repository

git clone https://github.com/yourusername/stock-analysis-dashboard.git
cd Stock Model Analysis


Create and activate a virtual environment

python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt

▶️ Run the Application

Start the Streamlit server:

streamlit run app.py


Open your browser and go to:

http://localhost:8501

📊 Example Outputs
📉 Candlestick Chart

Shows price fluctuations with open, high, low, and close data.

📈 Daily Profit/Loss Trend

Line chart showing daily percentage changes in stock closing price.

💰 Investment Simulation

Simulates how much a $1000 investment would have grown (or declined) over the past year.

(Add screenshots of charts and simulation results here for better presentation)

📈 Supported Stocks

Includes a preset selection of popular tickers such as:

AAPL, GOOGL, MSFT, COIN, AMZN, MRNA, NVAX, ARM, BNTX, AMD, NIO, SQ, LYFT, LI, JOBY, and more...


You can easily extend the list in the code to track additional stocks.

🔮 Future Improvements

 Allow custom ticker input (beyond predefined list).

 Add more timeframes (e.g., 5y, 10y, YTD).

 Compare multiple stocks in the same chart.

 Export charts and results as PDF/CSV reports.

 Add technical indicators (RSI, MACD, Moving Averages).

🤝 Contributing

Contributions, bug reports, and feature requests are welcome!
Steps to contribute:

Fork the repository

Create a new branch (feature/new-feature)

Commit your changes

Open a pull request

📜 License

This project is licensed under the MIT License – feel free to use, modify, and share.


