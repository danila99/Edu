import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import sys
import csv
import os
import numpy as np
import datetime as dt
import pandas as pd


cash_total = 1000000
orders_file = sys.argv[1]
print "orders from", orders_file
print "investing", cash_total


print "reading all symbols involved"
symbols = []
dates = []
with open(orders_file, 'rU') as f:
    csvdata = csv.reader(f)
    for arr in csvdata:
        symbols.append(arr[3])
        dates.append(dt.datetime(year=int(arr[0]), month=int(arr[1]), day=int(arr[2]), hour=16))
symbols = list(set(x for x in symbols))
print "symbols:", symbols


print "defining the time frame"
simulator_start_date = dates[0]
simulator_end_date = dates[-1]
index = du.getNYSEdays(simulator_start_date, simulator_end_date, dt.timedelta(hours=16))
print "from:", simulator_start_date, "to:", simulator_end_date


print "trades mock up"
trades = pd.DataFrame(0, index, symbols)
print "reading actual trades to DataFrame"
with open(orders_file, 'rU') as f:
    csvdata = csv.reader(f)
    for arr in csvdata:
        date = dt.datetime(year=int(arr[0]), month=int(arr[1]), day=int(arr[2]), hour=16)
        symbol = arr[3]
        multiplier = -1 if arr[4] == 'Sell' else 1
        shares = int(arr[5])
        trades[symbol][date] += shares * multiplier
print "shares put to trades"


print "reading close prices to DataFrame from Yahoo"
c_datable = da.DataAccess('Yahoo')
key_list = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
data_list = c_datable.get_data(index, symbols, key_list)
d_data = dict(zip(key_list, data_list))
df_close = d_data['close'].copy()
df_close = df_close.fillna(method='ffill')
df_close = df_close.fillna(method='bfill')


print "cash mock up; put initial cash to zero row"
cash = pd.DataFrame(0, index, ['_CASH'])
cash.set_value(index[0], "_CASH", cash_total)
print "reading cash to DataFrame using trades and close prices data"
for date, s in trades.iterrows():
    closes_on_date = df_close.loc[date]
    cash_on_date = cash.get_value(date, "_CASH") - np.dot(s, closes_on_date)
    cash.set_value(date, "_CASH", cash_on_date)


print "append cash to trades and close prices DataFrames"
df_close['_CASH'] = 1.0
trades['_CASH'] = cash


print "cumsum on trades"
trades = trades.cumsum(axis=0)
print "cumsum on portfolio"
portfolio = (trades * df_close).cumsum(axis=1)


fname, extension = os.path.splitext(orders_file)
values_fname = "values." + fname + ".csv"
print "writing portfolio values to a file:", values_fname
writer = csv.writer(open(values_fname, "wb"), delimiter=",")
for date in portfolio["_CASH"].index:
    line = [date.year, date.month, date.day, portfolio.loc[date]["_CASH"]]
    writer.writerow(line)

print "done."