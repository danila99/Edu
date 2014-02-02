import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import datetime as dt
import csv
import pandas.stats.moments as moments
import pandas as pd
import numpy as np
import copy


_orders_fname = "orders.csv"
_benchmark_symbol = "SPY"
_lookback = 20

def find_events(bands, symbols):
    index = bands.index
    with open(_orders_fname, "wb") as file:
        writer = csv.writer(file, delimiter=",")
        for i in range(_lookback + 1, len(index)):
            print "locating events at", index[i]
            for symbol in symbols:
                if symbol == _benchmark_symbol:
                    continue
                bollinger_today = bands[symbol].ix[index[i]]
                bollinger_yesterday = bands[symbol].ix[index[i-1]]
                bollinger_today_benchmark = bands[_benchmark_symbol].ix[index[i]]
                if bollinger_today < -2.0 and bollinger_yesterday >= -2.0 and bollinger_today_benchmark >= 1.2:
                    print "found event for:", symbol, "on:", index[i]
                    buy_date = index[i]
                    sell_date = index[i + 5] if len(index) > i + 5 else index[-1]
                    writer.writerow([buy_date.year, buy_date.month, buy_date.day, symbol, 'Buy', '100'])
                    writer.writerow([sell_date.year, sell_date.month, sell_date.day, symbol, 'Sell', '100'])

dt_start = dt.datetime(year=2008, month=1, day=1)
dt_end = dt.datetime(year=2009, month=12, day=31)
print "from", dt_start, 'to', dt_end

index = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
data_access = da.DataAccess('Yahoo')
symbols = data_access.get_symbols_from_list("sp5002012")
symbols.append(_benchmark_symbol)
print 'total symbols:', len(symbols), "starts with:", symbols[:20]

print 'getting data...'
ls_keys = ['close'] # 'actual_close'
ldf_data = data_access.get_data(index, symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))

print 'filling n/a with 1.0...'
for s_key in ls_keys:
    d_data[s_key] = d_data[s_key].fillna(method='ffill')
    d_data[s_key] = d_data[s_key].fillna(method='bfill')
    d_data[s_key] = d_data[s_key].fillna(1.0)

print "calculating rolling mean and std"
prices = d_data['close'].copy()
rolling_means = moments.rolling_mean(prices, _lookback, min_periods=_lookback)
rolling_stds = moments.rolling_std(prices, _lookback, min_periods=_lookback)

print "calculating Bollinger values"
bands = pd.DataFrame(0, index, symbols)
for s in symbols:
    bands[s] = (prices[s] - rolling_means[s]) / (rolling_stds[s])

print "finding Events for Bollinger data"
find_events(bands, symbols)

print "orders put to:", _orders_fname
print "done."