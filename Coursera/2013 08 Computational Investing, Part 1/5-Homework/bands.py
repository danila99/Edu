import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import sys
import csv
import os
import numpy as np
import datetime as dt
import pandas as pd
import pandas.stats.moments as moments
import matplotlib.pyplot as plt


assert len(sys.argv) > 1
symbol = sys.argv[1]
symbols = [symbol]
dt_start = dt.datetime(year=2010, month=1, day=1)
dt_end = dt.datetime(year=2010, month=12, day=31)
print "symbol:", symbol, "from", dt_start, 'to', dt_end

print "reading close prices to DataFrame from Yahoo"
index = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
c_datable = da.DataAccess('Yahoo')
key_list = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
data_list = c_datable.get_data(index, symbols, key_list)
d_data = dict(zip(key_list, data_list))
price = d_data['close'].copy()
price = price.fillna(method='ffill')
price = price.fillna(method='bfill')

print "calculating rolling mean and std"
rolling_mean = moments.rolling_mean(price, 20, min_periods=20)
rolling_std = moments.rolling_std(price, 20, min_periods=20)

print "generating graph"
plt.clf()
plt.plot(price.index, price[symbol].values, label=symbol)
plt.plot(price.index, rolling_mean[symbol].values)
#plt.plot(price.index, rolling_std[symbol].values)
plt.legend([symbol, 'Rolling Mean'])
plt.ylabel('Adjusted Close')
graph_file_name = symbol + ".png"
print "saving to", graph_file_name
plt.savefig(graph_file_name, format='png')

print "calculating Bollinger values"
bands = pd.DataFrame(0, index, symbols)
for s in symbols:
    bands[s] = (price[s] - rolling_mean[s]) / (rolling_std[s])

values_file_name = symbol + "-Bollinger.csv"
print "writing Bollinger values to:", values_file_name
with open(values_file_name, "wb") as file:
    writer = csv.writer(file, delimiter=",")
    for date in bands[symbol].index:
        line = [date.year, date.month, date.day, bands.loc[date][symbol]]
        writer.writerow(line)

print "done."