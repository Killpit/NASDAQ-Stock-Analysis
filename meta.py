import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

data = pd.read_csv("Users/META.csv") #use pwd command to locate the files in PyCharm and copy paste the output from this command
print(data.head())

#column insights
print(data.info())

#null value check
print(data.isnull())

#removing null values
data = data.dropna()

figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"],
                                        high=data["High"],
                                        low=data["Low"],
                                        close=data["Close"])])

figure.update_layout(title= "Twitter Stock Prices Over the Year",
                     xaxis_rangeslider_visible=False)

figure.show()

figure = px.bar(data,
                x="Date",
                y="Close",
                color="Close")
figure.update_xaxes(rangeslider_visible = True)
figure.show()

figure = px.bar(data, x="Date", y="Close", color="Close")
figure.update_xaxes(rangeslider_visible=True)
figure.update_layout(title="Twitter Stock Prices Over the Years",
                     xaxis_rangeslider_visible=False)

figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=2, label="2y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure.show()

data["Date"] = pd.to_datetime(data["Date"],
                              format = '%Y-%m-%d')
data['Year'] = data['Date'].dt.year
data["Month"] = data["Date"].dt.month
fig = px.line(data,
              x="Month",
              y="Close",
              color='Year',
              title="Complete Timeline of Twitter")
fig.show()
