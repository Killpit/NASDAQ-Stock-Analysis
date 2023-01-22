
#importing necessary libraries

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

#collecting stock data

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d1 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AMZN',
                   start=start_date,
                   end=end_date,
                   progress=False)

data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())

#Candlestick

figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], high=data["High"],
                                        low=data["Low"], close=data["Close"])])
figure.update_layout(title = "Amazon Stock Price Analysis",
                     xaxis_rangeslider_visible = False)
figure.show()

#barplot

figure = px.bar(data, x="Date", y="Close")
figure.show()

#line graph

figure = px.line(data, x='Date', y='Close',
                 title='Stock Market Analysis with Rangeslider')
figure.update_xaxes(rangeslider_visible=True)
figure.show()

#line graph with time period selectors

figure = px.line(data, x='Date', y='Close',
                 title='Stock Market Analysis with Time Period Selectors')

#separating line graph to various time periods

figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure.show()

#scatterplot

figure = px.scatter(data, x='Date', y='Close', range_x=['2021-07-12', '2022-07-11'],
                    title="Stock Market Analysis by Hiding Weekend Gaps")
figure.update_xaxes(
    rangebreaks=[dict(bounds=["sat", "sun"])]
)
figure.show()
