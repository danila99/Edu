import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy
import sys
import pandas.stats.moments as moments
import QSTK.qstkstudy.Events as ev
import QSTK.qstkstudy.EventProfiler as ep

_benchmark_symbol = "SPY"
_lookback = 20

def find_events(bands, symbols):
    df_events = copy.deepcopy(bands)
    df_events = df_events * np.NAN
    index = bands.index

    for symbol in symbols:
        if symbol == _benchmark_symbol:
            continue
        print "locating events for", symbol
        for i in range(_lookback + 1, len(index)):
            bollinger_today = bands[symbol].ix[index[i]]
            bollinger_yesterday = bands[symbol].ix[index[i-1]]
            bollinger_today_benchmark = bands[_benchmark_symbol].ix[index[i]]
            if bollinger_today < -2.0 and bollinger_yesterday >= -2.0 and bollinger_today_benchmark >= 1.4:
                df_events[symbol].ix[index[i]] = 1

    return df_events

data_access = da.DataAccess('Yahoo')
symbols = data_access.get_symbols_from_list("sp5002012")
symbols.append(_benchmark_symbol)
print 'total symbols:', len(symbols), "starts with:", symbols[:20]

dt_start = dt.datetime(year=2008, month=1, day=1)
dt_end = dt.datetime(year=2009, month=12, day=31)
print "from", dt_start, 'to', dt_end

print "reading close prices to DataFrame from Yahoo"
index = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

key_list = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
data_list = data_access.get_data(index, symbols, key_list)
d_data = dict(zip(key_list, data_list))
prices = d_data['close'].copy()
prices = prices.fillna(method='ffill')
prices = prices.fillna(method='bfill')

print "calculating rolling mean and std"
rolling_means = moments.rolling_mean(prices, _lookback, min_periods=_lookback)
rolling_stds = moments.rolling_std(prices, _lookback, min_periods=_lookback)

print "calculating Bollinger values"
bands = pd.DataFrame(0, index, symbols)
for s in symbols:
    bands[s] = (prices[s] - rolling_means[s]) / (rolling_stds[s])

print "finding Events for Bollinger data"
df_events = find_events(bands, symbols)

print "creating Study"
ep.eventprofiler(df_events, d_data,
                 i_lookback=_lookback,
                 i_lookforward=_lookback,
                 s_filename='BollingerStudy_1.4.pdf',
                 b_market_neutral=True,
                 b_errorbars=True,
                 s_market_sym=_benchmark_symbol)

print "done."