import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#   //             //
#  // Other notes // 
# //             //
start = dt.date(2018, 12, 31)  # setup the start date
end = dt.datetime(2019, 4, 24)  # setup the end date

df = web.DataReader('AMZN', 'yahoo', start, end)  # ticker, source

df.to_csv('AMZN.cvs')  # df to cvs format & assigning filename

df.plot()  # plots the graph using pandas
plt.show()  # actually shows the plot

style.use('ggplot')  # adds style to the plot

df = pd.read_csv('AMZN.cvs', parse_dates=True, index_col=0)  # creates a csv file of the aap call

print(df[['Open', 'High']].head())

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()  # creates a new column called 100ma

print(df.tail())

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)  # (row, column) -> six rolls, 1 column
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=5, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()


